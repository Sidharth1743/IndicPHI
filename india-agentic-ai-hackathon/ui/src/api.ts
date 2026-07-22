import type {
  MetaResponse,
  PipelineEvent,
  ReplayResponse,
  RunSnapshot,
  StartRunRequest,
  StartRunResponse,
} from './types'

async function parseJson<T>(res: Response): Promise<T> {
  if (!res.ok) {
    const text = await res.text().catch(() => '')
    throw new Error(text || `${res.status} ${res.statusText}`)
  }
  return res.json() as Promise<T>
}

function normalizeMeta(raw: Record<string, unknown>): MetaResponse {
  const runsRaw = (raw.past_runs ?? raw.runs ?? []) as Array<Record<string, string>>
  const past_runs = runsRaw.map((r) => ({
    id: String(r.id ?? r.run_id ?? ''),
    label: r.label ?? r.run_id ?? r.id,
    status: r.status,
    created_at: r.created_at,
  }))
  return {
    languages: (raw.languages as MetaResponse['languages']) ?? [],
    models: raw.models as MetaResponse['models'],
    past_runs: past_runs.filter((r) => r.id),
  }
}

export async function fetchMeta(): Promise<MetaResponse | null> {
  try {
    const res = await fetch('/api/meta')
    const raw = await parseJson<Record<string, unknown>>(res)
    return normalizeMeta(raw)
  } catch {
    return null
  }
}

export async function startRun(body: StartRunRequest): Promise<StartRunResponse> {
  const res = await fetch('/api/runs', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(body),
  })
  return parseJson<StartRunResponse>(res)
}

export async function stopRun(runId: string): Promise<void> {
  await fetch(`/api/runs/${encodeURIComponent(runId)}/stop`, { method: 'POST' })
}

export async function fetchRun(runId: string): Promise<RunSnapshot> {
  const res = await fetch(`/api/runs/${encodeURIComponent(runId)}`)
  return parseJson<RunSnapshot>(res)
}

export async function fetchReplay(runId: string): Promise<ReplayResponse> {
  const res = await fetch(`/api/replay/${encodeURIComponent(runId)}`, {
    method: 'POST',
  })
  return parseJson<ReplayResponse>(res)
}

/** Subscribe to SSE stage events with auto-reconnect. Returns an unsubscribe function. */
export function streamRun(
  runId: string,
  onEvent: (event: PipelineEvent) => void,
  onError?: (err: Error) => void,
): () => void {
  let closed = false
  let es: EventSource | null = null
  let reconnectTimer: number | null = null

  const handleMessage = (raw: MessageEvent) => {
    try {
      const data = JSON.parse(String(raw.data)) as PipelineEvent
      onEvent(data)
      if (data.type === 'done' || data.type === 'error') {
        closed = true
        es?.close()
      }
    } catch (err) {
      onError?.(err instanceof Error ? err : new Error(String(err)))
    }
  }

  const connect = () => {
    if (closed) return
    es?.close()
    es = new EventSource(`/api/runs/${encodeURIComponent(runId)}/stream`)
    es.onmessage = handleMessage
    for (const name of ['stage', 'repair', 'progress', 'summary', 'done', 'error']) {
      es.addEventListener(name, handleMessage)
    }
    es.onerror = () => {
      if (closed) return
      es?.close()
      // Transient disconnect — reconnect unless terminal event already received.
      reconnectTimer = window.setTimeout(connect, 800)
    }
  }

  connect()

  return () => {
    closed = true
    if (reconnectTimer != null) window.clearTimeout(reconnectTimer)
    es?.close()
  }
}
