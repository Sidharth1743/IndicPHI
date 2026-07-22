import { ChevronDown, Circle, Loader2, Play, RotateCcw, Square } from 'lucide-react'
import { useEffect, useId, useRef, useState } from 'react'
import type { LanguageOption, PastRun } from '../types'

interface ControlsProps {
  numDocs: number
  onNumDocs: (n: number) => void
  languages: LanguageOption[]
  selectedLangs: string[]
  onSelectedLangs: (codes: string[]) => void
  pastRuns: PastRun[]
  replayId: string
  onReplayId: (id: string) => void
  statusLabel: string
  statusTone: string
  busy: boolean
  onRunLive: () => void
  onReplay: () => void
  onStop: () => void
}

export function Controls({
  numDocs,
  onNumDocs,
  languages,
  selectedLangs,
  onSelectedLangs,
  pastRuns,
  replayId,
  onReplayId,
  statusLabel,
  statusTone,
  busy,
  onRunLive,
  onReplay,
  onStop,
}: ControlsProps) {
  const [open, setOpen] = useState(false)
  const panelRef = useRef<HTMLDivElement>(null)
  const listId = useId()

  useEffect(() => {
    if (!open) return
    const onDoc = (e: MouseEvent) => {
      if (!panelRef.current?.contains(e.target as Node)) setOpen(false)
    }
    document.addEventListener('mousedown', onDoc)
    return () => document.removeEventListener('mousedown', onDoc)
  }, [open])

  const toggleLang = (code: string) => {
    if (selectedLangs.includes(code)) {
      if (selectedLangs.length <= 1) return
      onSelectedLangs(selectedLangs.filter((c) => c !== code))
    } else {
      onSelectedLangs([...selectedLangs, code])
    }
  }

  const langSummary =
    selectedLangs.length === 0
      ? 'Select languages'
      : selectedLangs.length <= 3
        ? selectedLangs.join(', ')
        : `${selectedLangs.slice(0, 2).join(', ')} +${selectedLangs.length - 2}`

  return (
    <section className="controls" aria-label="Pipeline controls">
      <div className="field">
        <label htmlFor="num-docs">Documents</label>
        <input
          id="num-docs"
          type="number"
          min={1}
          max={50}
          value={numDocs}
          disabled={busy}
          onChange={(e) => onNumDocs(Math.max(1, Math.min(50, Number(e.target.value) || 1)))}
        />
      </div>

      <div className="field lang-select" ref={panelRef}>
        <label id={`${listId}-label`}>Languages</label>
        <button
          type="button"
          className="lang-trigger"
          aria-labelledby={`${listId}-label`}
          aria-expanded={open}
          aria-controls={listId}
          disabled={busy || languages.length === 0}
          onClick={() => setOpen((v) => !v)}
        >
          <span>{langSummary}</span>
          <ChevronDown size={16} strokeWidth={1.75} aria-hidden />
        </button>
        {open && (
          <div className="lang-panel" id={listId} role="listbox" aria-multiselectable>
            {languages.map((lang) => (
              <label key={lang.code} className="lang-option">
                <input
                  type="checkbox"
                  checked={selectedLangs.includes(lang.code)}
                  onChange={() => toggleLang(lang.code)}
                />
                <span>
                  {lang.name}{' '}
                  <span style={{ color: 'var(--ink-faint)', fontFamily: 'var(--font-mono)', fontSize: '0.75rem' }}>
                    {lang.code}
                  </span>
                </span>
              </label>
            ))}
          </div>
        )}
      </div>

      <div className="field">
        <label htmlFor="replay-run">Past run</label>
        <select
          id="replay-run"
          className="replay-select"
          value={replayId}
          disabled={busy || pastRuns.length === 0}
          onChange={(e) => onReplayId(e.target.value)}
        >
          {pastRuns.length === 0 ? (
            <option value="">No past runs</option>
          ) : (
            pastRuns.map((run) => (
              <option key={run.id} value={run.id}>
                {run.label || run.id}
                {run.status ? ` · ${run.status}` : ''}
              </option>
            ))
          )}
        </select>
      </div>

      <div className="controls-actions">
        <button type="button" className="btn btn-primary" disabled={busy} onClick={onRunLive}>
          {busy && statusTone === 'live' ? (
            <Loader2 size={16} strokeWidth={1.75} className="spin" aria-hidden />
          ) : (
            <Play size={16} strokeWidth={1.75} aria-hidden />
          )}
          Run live
        </button>
        <button
          type="button"
          className="btn btn-secondary"
          disabled={busy || !replayId}
          onClick={onReplay}
        >
          <RotateCcw size={16} strokeWidth={1.75} aria-hidden />
          Replay
        </button>
        {busy && (
          <button type="button" className="btn btn-stop" onClick={onStop}>
            <Square size={14} strokeWidth={1.75} fill="currentColor" aria-hidden />
            Stop
          </button>
        )}
        <span className="status-pill" data-tone={statusTone} title={statusLabel}>
          <Circle size={8} fill="currentColor" strokeWidth={0} aria-hidden />
          <span className="status-text">{statusLabel}</span>
        </span>
      </div>
    </section>
  )
}
