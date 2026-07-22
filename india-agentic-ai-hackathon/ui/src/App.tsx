import { useCallback, useEffect, useMemo, useRef, useState } from 'react'
import { fetchMeta, fetchReplay, fetchRun, startRun, stopRun, streamRun } from './api'
import { ActivityFeed, type ActivityEntry } from './components/ActivityFeed'
import { Controls } from './components/Controls'
import { PipelineGraph } from './components/PipelineGraph'
import { StageInspector } from './components/StageInspector'
import { SummaryBar } from './components/SummaryBar'
import { DEFAULT_DEMO_LANGS, DEFAULT_LANGUAGES, REPLAY_TARGET_MS, STAGE_IDS } from './stages'
import type {
  AppMode,
  LanguageOption,
  PastRun,
  PipelineEvent,
  RunSnapshot,
  StageId,
  StageSnapshot,
  StageStatus,
  SummaryMetrics,
} from './types'

function emptyStatuses(): Record<StageId, StageStatus> {
  return {
    seed: 'idle',
    generate: 'idle',
    translate: 'idle',
    judge: 'idle',
    audit: 'idle',
    curate: 'idle',
    export: 'idle',
  }
}

function isStageId(v: string | undefined): v is StageId {
  return !!v && (STAGE_IDS as string[]).includes(v)
}

function eventStageId(ev: PipelineEvent): StageId | null {
  const raw = ev.stage ?? ev.node_id
  return isStageId(raw) ? raw : null
}

function nowTime() {
  return new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit', second: '2-digit' })
}

export default function App() {
  const [languages, setLanguages] = useState<LanguageOption[]>(DEFAULT_LANGUAGES)
  const [pastRuns, setPastRuns] = useState<PastRun[]>([])
  const [metaError, setMetaError] = useState<string | null>(null)

  const [numDocs, setNumDocs] = useState(8)
  const [selectedLangs, setSelectedLangs] = useState<string[]>(DEFAULT_DEMO_LANGS)
  const [replayId, setReplayId] = useState('')

  const [mode, setMode] = useState<AppMode>('idle')
  const [runId, setRunId] = useState<string | null>(null)
  const [statuses, setStatuses] = useState(emptyStatuses)
  const [stages, setStages] = useState<Partial<Record<StageId, StageSnapshot>>>({})
  const [selected, setSelected] = useState<StageId | null>('seed')
  const [repairing, setRepairing] = useState(false)
  const [repairPath, setRepairPath] = useState<StageId[]>([])
  const [summary, setSummary] = useState<SummaryMetrics>({})
  const [error, setError] = useState<string | null>(null)
  const [warning, setWarning] = useState<string | null>(null)
  const [activeMetric, setActiveMetric] = useState<string | null>(null)
  const [activity, setActivity] = useState<ActivityEntry[]>([])
  const [liveActivity, setLiveActivity] = useState('')

  const cancelRef = useRef<(() => void) | null>(null)
  const pollRef = useRef<number | null>(null)
  const timersRef = useRef<number[]>([])
  const modeRef = useRef(mode)
  const lastActivityRef = useRef('')
  const activitySeq = useRef(0)
  modeRef.current = mode

  const busy = mode === 'live' || mode === 'replay'

  const pushActivity = useCallback((message: string, tone: ActivityEntry['tone'] = 'info') => {
    if (!message || message === lastActivityRef.current) return
    lastActivityRef.current = message
    activitySeq.current += 1
    setActivity((prev) => [
      { id: `${activitySeq.current}`, time: nowTime(), message, tone },
      ...prev.slice(0, 24),
    ])
    setLiveActivity(message)
  }, [])

  const clearScheduled = useCallback(() => {
    timersRef.current.forEach((t) => window.clearTimeout(t))
    timersRef.current = []
    cancelRef.current?.()
    cancelRef.current = null
    if (pollRef.current != null) {
      window.clearInterval(pollRef.current)
      pollRef.current = null
    }
  }, [])

  const resetPipeline = useCallback(() => {
    setStatuses(emptyStatuses())
    setStages({})
    setSummary({})
    setRepairing(false)
    setRepairPath([])
    setError(null)
    setWarning(null)
    setActiveMetric(null)
    setActivity([])
    setLiveActivity('')
    lastActivityRef.current = ''
    setSelected('seed')
  }, [])

  const mergeInspector = useCallback(
    (stageId: StageId, insp: NonNullable<PipelineEvent['inspector']>, message?: string) => {
      setStages((prev) => ({
        ...prev,
        [stageId]: {
          id: stageId,
          status: prev[stageId]?.status ?? 'running',
          model: insp.model ?? prev[stageId]?.model,
          engine: insp.engine ?? prev[stageId]?.engine,
          preview: insp.preview ?? insp.sample?.join('\n') ?? prev[stageId]?.preview,
          fail_reason: insp.fail_reason ?? prev[stageId]?.fail_reason,
          counts: insp.counts ?? prev[stageId]?.counts,
          message: message ?? prev[stageId]?.message,
        },
      }))
    },
    [],
  )

  const applySnapshot = useCallback(
    (snap: RunSnapshot) => {
      if (snap.stages?.length) {
        setStatuses((prev) => {
          const next = { ...prev }
          for (const s of snap.stages!) {
            next[s.id] = s.status
          }
          return next
        })
        setStages((prev) => {
          const next = { ...prev }
          for (const s of snap.stages!) {
            next[s.id] = {
              id: s.id,
              status: s.status,
              model: s.model,
              counts: s.counts,
              ...next[s.id],
            }
          }
          return next
        })
        if (snap.active_stage) setSelected(snap.active_stage)
      }
      if (snap.repair_path?.length) setRepairPath(snap.repair_path)
      setRepairing(Boolean(snap.repair_active))
      if (snap.summary) {
        setSummary((prev) => ({
          ...prev,
          ...snap.summary,
          entity_coverage:
            snap.summary?.entity_coverage ?? snap.summary?.s4_entity_coverage ?? prev.entity_coverage,
        }))
      }
      if (snap.active_stage && snap.inspector) {
        mergeInspector(snap.active_stage, snap.inspector, snap.activity)
      }
      if (snap.activity) {
        pushActivity(snap.activity, snap.repair_active ? 'repair' : 'info')
      }
    },
    [mergeInspector, pushActivity],
  )

  const applyEvent = useCallback(
    (ev: PipelineEvent) => {
      const stageId = eventStageId(ev)

      if (ev.type === 'repair' || ev.repair_path?.length) {
        setRepairing(true)
        if (ev.repair_path?.length) setRepairPath(ev.repair_path)
        else if (ev.repair_nodes?.length)
          setRepairPath(['judge', 'generate', 'translate', 'judge'])
        pushActivity(ev.message ?? 'Repair loop: regenerate → translate → re-judge', 'repair')
      }

      if (ev.type === 'stage' || ev.type === 'progress' || ev.type === 'repair') {
        if (stageId) {
          const status = ev.status ?? (ev.type === 'repair' ? 'repairing' : 'running')
          setStatuses((prev) => ({ ...prev, [stageId]: status }))
          setStages((prev) => ({
            ...prev,
            [stageId]: {
              id: stageId,
              status,
              engine: ev.engine ?? ev.inspector?.engine ?? prev[stageId]?.engine,
              model: ev.model ?? ev.inspector?.model ?? prev[stageId]?.model,
              counts: ev.counts ?? ev.inspector?.counts ?? prev[stageId]?.counts,
              preview:
                ev.preview ??
                ev.inspector?.preview ??
                ev.inspector?.sample?.join('\n') ??
                prev[stageId]?.preview,
              fail_reason: ev.fail_reason ?? ev.inspector?.fail_reason ?? prev[stageId]?.fail_reason,
              message: ev.message ?? prev[stageId]?.message,
            },
          }))
          setSelected(stageId)
          if (ev.message) pushActivity(ev.message, status === 'repairing' ? 'repair' : 'info')
          if (status === 'ok' && stageId !== 'generate' && !ev.repair_path?.length) {
            setRepairing(false)
          }
          if (status === 'repairing') setRepairing(true)
          if (status === 'failed') pushActivity(`${stageId} failed`, 'fail')
          if (status === 'ok') pushActivity(`${stageId} complete`, 'ok')
        }
        if (stageId && ev.inspector) mergeInspector(stageId, ev.inspector, ev.message)
      }

      if (ev.type === 'summary' || ev.summary) {
        if (ev.summary) {
          setSummary((prev) => ({
            ...prev,
            ...ev.summary,
            entity_coverage:
              ev.summary?.entity_coverage ?? ev.summary?.s4_entity_coverage ?? prev.entity_coverage,
          }))
        }
        setRepairing(false)
        setRepairPath([])
      }

      if (ev.type === 'done') {
        if (ev.summary) setSummary((prev) => ({ ...prev, ...ev.summary }))
        setRepairing(false)
        setRepairPath([])
        const doneStatus = (ev as { status?: string }).status
        const cancelled = doneStatus === 'cancelled'
        const failed = doneStatus === 'failed'
        const failStage = eventStageId(ev)
        const msg = (ev as { message?: string }).message

        if (cancelled) {
          setMode('idle')
          pushActivity(msg ?? 'Run stopped', 'info')
        } else if (failed) {
          setMode('partial')
          setWarning(msg ?? 'Pipeline stopped — see failed stage for details')
          if (failStage) {
            setSelected(failStage)
            setStatuses((prev) => ({ ...prev, [failStage]: 'failed' }))
            setStages((prev) => ({
              ...prev,
              [failStage]: {
                ...prev[failStage],
                id: failStage,
                status: 'failed',
                fail_reason:
                  ev.fail_reason ??
                  (ev as { fail_reason?: string }).fail_reason ??
                  msg,
                message: msg,
              },
            }))
          }
          pushActivity(msg ?? 'Pipeline failed at late stage', 'fail')
        } else {
          setMode('done')
          pushActivity('Pipeline complete', 'ok')
        }

        setStatuses((prev) => {
          const next: Record<StageId, StageStatus> = { ...prev }
          for (const id of STAGE_IDS) {
            if (next[id] === 'running' || next[id] === 'repairing') next[id] = 'ok'
          }
          if (failStage) next[failStage] = 'failed'
          return next
        })
      }

      if (ev.type === 'error') {
        setError(ev.message || ev.fail_reason || 'Pipeline error')
        setMode('error')
        setRepairing(false)
        setRepairPath([])
        pushActivity(ev.message ?? 'Pipeline error', 'fail')
        if (stageId) setStatuses((prev) => ({ ...prev, [stageId]: 'failed' }))
      }
    },
    [mergeInspector, pushActivity],
  )

  useEffect(() => {
    let cancelled = false
    ;(async () => {
      const meta = await fetchMeta()
      if (cancelled) return
      if (!meta) {
        setMetaError('API unavailable — start the FastAPI server on :8765 for live/replay data.')
        return
      }
      setMetaError(null)
      if (meta.languages?.length) {
        setLanguages(meta.languages)
        setSelectedLangs((prev) => {
          const codes = new Set(meta.languages.map((l) => l.code))
          const kept = prev.filter((c) => codes.has(c))
          return kept.length ? kept : meta.languages.slice(0, 3).map((l) => l.code)
        })
      }
      const runs = meta.past_runs ?? []
      setPastRuns(runs)
      if (runs[0]) setReplayId(runs[0].id)
    })()
    return () => {
      cancelled = true
    }
  }, [])

  const playReplayEvents = useCallback(
    (events: PipelineEvent[], durationMs = REPLAY_TARGET_MS) => {
      clearScheduled()
      resetPipeline()
      setMode('replay')
      pushActivity(`Replaying run (${Math.round(durationMs / 1000)}s)`, 'info')

      if (!events.length) {
        setMode('done')
        return
      }

      let schedule: { ev: PipelineEvent; at: number }[] = []
      let cursor = 0
      for (const ev of events) {
        if (ev.at != null) cursor = ev.at
        else if (ev.t != null) cursor = ev.t * 1000
        else if (ev.delay_ms != null) cursor += ev.delay_ms
        else cursor += durationMs / events.length
        schedule.push({ ev, at: cursor })
      }
      const last = schedule[schedule.length - 1]?.at ?? durationMs
      if (last > 0 && Math.abs(last - durationMs) > 800) {
        const scale = durationMs / last
        schedule = schedule.map((s) => ({ ...s, at: s.at * scale }))
      }

      for (const item of schedule) {
        const t = window.setTimeout(() => applyEvent(item.ev), item.at)
        timersRef.current.push(t)
      }

      const hasDone = events.some((e) => e.type === 'done')
      if (!hasDone) {
        const t = window.setTimeout(() => applyEvent({ type: 'done' }), durationMs + 200)
        timersRef.current.push(t)
      }
    },
    [applyEvent, clearScheduled, pushActivity, resetPipeline],
  )

  const handleReplay = useCallback(
    async (id?: string) => {
      const target = id || replayId
      if (!target) return
      clearScheduled()
      setError(null)
      setRunId(target)
      try {
        const res = await fetchReplay(target)
        playReplayEvents(res.events ?? [], res.duration_ms ?? REPLAY_TARGET_MS)
      } catch (err) {
        setMode('error')
        setError(err instanceof Error ? err.message : String(err))
      }
    },
    [clearScheduled, playReplayEvents, replayId],
  )

  const startLivePoll = useCallback(
    (id: string) => {
      if (pollRef.current != null) window.clearInterval(pollRef.current)
      pollRef.current = window.setInterval(() => {
        void fetchRun(id)
          .then(applySnapshot)
          .catch(() => undefined)
      }, 400)
    },
    [applySnapshot],
  )

  const handleRunLive = useCallback(async () => {
    clearScheduled()
    resetPipeline()
    setError(null)
    setMode('live')
    pushActivity('Starting live pipeline run…', 'info')
    try {
      const res = await startRun({
        num_docs: numDocs,
        language_codes: selectedLangs,
      })
      setRunId(res.run_id)
      startLivePoll(res.run_id)
      const stop = streamRun(
        res.run_id,
        (ev) => applyEvent(ev),
        (err) => {
          if (modeRef.current === 'done' || modeRef.current === 'error' || modeRef.current === 'idle')
            return
          console.warn(err)
        },
      )
      cancelRef.current = stop
    } catch (err) {
      setMode('error')
      setError(err instanceof Error ? err.message : String(err))
    }
  }, [applyEvent, clearScheduled, numDocs, pushActivity, resetPipeline, selectedLangs, startLivePoll])

  const handleStop = useCallback(async () => {
    clearScheduled()
    if (runId && mode === 'live') {
      try {
        await stopRun(runId)
        pushActivity('Stop requested — finishing current stage…', 'info')
      } catch {
        pushActivity('Stopped (client disconnect)', 'info')
      }
    } else {
      pushActivity('Stopped replay', 'info')
    }
    setMode('idle')
    setRepairing(false)
    setRepairPath([])
  }, [clearScheduled, mode, pushActivity, runId])

  useEffect(() => () => clearScheduled(), [clearScheduled])

  const statusLabel = useMemo(() => {
    if (liveActivity && (mode === 'live' || mode === 'replay')) return liveActivity
    if (mode === 'live') return runId ? `live · ${runId}` : 'starting…'
    if (mode === 'replay') return runId ? `replay · ${runId}` : 'replaying…'
    if (mode === 'done') return runId ? `done · ${runId}` : 'done'
    if (mode === 'partial') return runId ? `partial · ${runId}` : 'partial'
    if (mode === 'error') return 'error'
    return 'idle'
  }, [liveActivity, mode, runId])

  const statusTone = repairing ? 'repairing' : mode

  const selectedSnap = selected ? stages[selected] : undefined

  return (
    <div className="app">
      <header className="header">
        <h1>HackGrid</h1>
        <p>Indic PHI synthetic data generation — seed to curated export.</p>
      </header>

      {metaError && <div className="banner-info">{metaError}</div>}
      {warning && <div className="banner-warn">{warning}</div>}
      {error && <div className="banner-error">{error}</div>}

      <Controls
        numDocs={numDocs}
        onNumDocs={setNumDocs}
        languages={languages}
        selectedLangs={selectedLangs}
        onSelectedLangs={setSelectedLangs}
        pastRuns={pastRuns}
        replayId={replayId}
        onReplayId={setReplayId}
        statusLabel={statusLabel}
        statusTone={statusTone}
        busy={busy}
        onRunLive={() => void handleRunLive()}
        onReplay={() => void handleReplay()}
        onStop={() => void handleStop()}
      />

      <PipelineGraph
        statuses={statuses}
        selected={selected}
        repairing={repairing}
        repairPath={repairPath}
        onSelect={setSelected}
      />

      <div className="detail-row">
        <StageInspector
          stageId={selected}
          snapshot={selectedSnap}
          fallbackStatus={selected ? statuses[selected] : undefined}
        />
        <ActivityFeed entries={activity} />
      </div>

      <SummaryBar
        summary={summary}
        activeMetric={activeMetric}
        onFocusStage={(id) => {
          setSelected(id)
          setActiveMetric(
            id === 'curate'
              ? 'curated'
              : id === 'judge'
                ? 's5'
                : id === 'audit'
                  ? 's6'
                  : id === 'generate'
                    ? 'entity'
                    : null,
          )
        }}
      />
    </div>
  )
}
