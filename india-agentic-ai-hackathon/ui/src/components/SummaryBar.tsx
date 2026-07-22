import type { StageId, SummaryMetrics } from '../types'

interface SummaryBarProps {
  summary: SummaryMetrics
  onFocusStage?: (id: StageId) => void
  activeMetric?: string | null
}

function fmtRate(v?: number) {
  if (v == null || Number.isNaN(v)) return '—'
  if (v <= 1) return `${Math.round(v * 100)}%`
  return `${Math.round(v)}%`
}

function fmtNum(v?: number) {
  if (v == null || Number.isNaN(v)) return '—'
  return String(v)
}

const METRICS: {
  key: string
  label: string
  stage?: StageId
  value: (s: SummaryMetrics) => string
}[] = [
  {
    key: 'curated',
    label: 'Curated',
    stage: 'curate',
    value: (s) => fmtNum(s.curated),
  },
  {
    key: 'failed',
    label: 'Failed',
    stage: 'judge',
    value: (s) => fmtNum(s.failed ?? s.hard_fails),
  },
  {
    key: 'recovered',
    label: 'Recovered',
    stage: 'generate',
    value: (s) => fmtNum(s.recovered),
  },
  {
    key: 's5',
    label: 'S5 pass',
    stage: 'judge',
    value: (s) => fmtRate(s.s5_pass_rate),
  },
  {
    key: 's6',
    label: 'S6 pass',
    stage: 'audit',
    value: (s) => fmtRate(s.s6_pass_rate),
  },
  {
    key: 'entity',
    label: 'Entity coverage',
    stage: 'generate',
    value: (s) => fmtRate(s.entity_coverage ?? s.s4_entity_coverage),
  },
]

export function SummaryBar({ summary, onFocusStage, activeMetric }: SummaryBarProps) {
  return (
    <section className="summary-bar" aria-label="Run summary">
      {METRICS.map((m) => (
        <button
          key={m.key}
          type="button"
          className="summary-metric"
          data-active={activeMetric === m.key ? 'true' : 'false'}
          onClick={() => m.stage && onFocusStage?.(m.stage)}
        >
          <span className="metric-value">{m.value(summary)}</span>
          <span className="metric-label">{m.label}</span>
        </button>
      ))}
    </section>
  )
}
