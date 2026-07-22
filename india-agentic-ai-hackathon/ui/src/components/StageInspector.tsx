import { STAGE_DEFS } from '../stages'
import type { StageId, StageSnapshot, StageStatus } from '../types'

interface StageInspectorProps {
  stageId: StageId | null
  snapshot?: StageSnapshot
  fallbackStatus?: StageStatus
}

function formatCounts(counts?: Record<string, number>) {
  if (!counts || Object.keys(counts).length === 0) return null
  return Object.entries(counts).map(([key, value]) => (
    <div key={key} className="count-item">
      <span>{key.replace(/_/g, ' ')}</span>
      {typeof value === 'number' && value <= 1 && value > 0 && key.includes('rate')
        ? `${Math.round(value * 100)}%`
        : value}
    </div>
  ))
}

export function StageInspector({ stageId, snapshot, fallbackStatus }: StageInspectorProps) {
  if (!stageId) {
    return (
      <section className="inspector" aria-label="Stage inspector">
        <p className="inspector-empty">Select a stage to inspect model, counts, and preview.</p>
      </section>
    )
  }

  const def = STAGE_DEFS.find((s) => s.id === stageId)
  const status = snapshot?.status ?? fallbackStatus ?? 'idle'
  const engine = snapshot?.engine || snapshot?.model || def?.callout || '—'
  const preview = snapshot?.preview
  const failReason = snapshot?.fail_reason
  const counts = formatCounts(snapshot?.counts)
  const rowsDone = snapshot?.counts?.rows_done
  const rowsTotal = snapshot?.counts?.rows_total
  const pct = snapshot?.counts?.pct

  return (
    <section className="inspector" aria-label="Stage inspector">
      <div className="inspector-head">
        <h2>
          {def?.label ?? stageId}{' '}
          <span className="inspector-stage-id">{def?.stages}</span>
        </h2>
        <div className="inspector-meta" data-status={status}>
          {status}
          {snapshot?.message ? ` · ${snapshot.message}` : ''}
        </div>
      </div>

      {rowsTotal != null && rowsTotal > 0 && (
        <div className="progress-bar-wrap" aria-label="Row progress">
          <div className="progress-bar">
            <div
              className="progress-fill"
              style={{ width: `${Math.min(100, pct ?? (rowsDone! / rowsTotal) * 100)}%` }}
            />
          </div>
          <span className="progress-label">
            {rowsDone ?? 0} / {rowsTotal} rows
            {pct != null ? ` (${pct}%)` : ''}
          </span>
        </div>
      )}

      <div className="inspector-grid">
        <div className="inspector-block">
          <h3>Engine</h3>
          <p>{engine}</p>
          {def?.callout && engine !== def.callout && (
            <p className="inspector-hint">{def.callout}</p>
          )}
          {counts && (
            <>
              <h3>Counts</h3>
              <div className="counts-row">{counts}</div>
            </>
          )}
        </div>

        <div className="inspector-block">
          <h3>{failReason ? 'Fail reason' : 'Preview'}</h3>
          {failReason ? (
            <p className="fail-reason">{failReason}</p>
          ) : preview ? (
            <pre>{preview}</pre>
          ) : (
            <p className="inspector-hint">No preview yet — waiting for stage output…</p>
          )}
        </div>
      </div>
    </section>
  )
}
