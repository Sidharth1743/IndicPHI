export type StageId =
  | 'seed'
  | 'generate'
  | 'translate'
  | 'judge'
  | 'audit'
  | 'curate'
  | 'export'

export type StageStatus = 'idle' | 'running' | 'ok' | 'failed' | 'repairing'

export type AppMode = 'idle' | 'live' | 'replay' | 'done' | 'error' | 'partial'

export interface LanguageOption {
  code: string
  name: string
  script?: string
}

export interface ModelBlurb {
  stage: StageId
  label: string
  engine: string
}

export interface PastRun {
  id: string
  label?: string
  status?: 'ok' | 'failed' | 'partial' | string
  created_at?: string
  num_docs?: number
  language_codes?: string[]
}

export interface MetaResponse {
  languages: LanguageOption[]
  models?: ModelBlurb[]
  past_runs: PastRun[]
}

export interface StartRunRequest {
  num_docs: number
  language_codes: string[]
  config?: string
}

export interface StartRunResponse {
  run_id: string
  mode: string
}

export interface StageSnapshot {
  id: StageId
  status: StageStatus
  engine?: string
  model?: string
  counts?: Record<string, number>
  preview?: string
  fail_reason?: string
  message?: string
}

export interface SummaryMetrics {
  curated?: number
  failed?: number
  recovered?: number
  generated?: number
  translated?: number
  soft_fails?: number
  hard_fails?: number
  s5_pass_rate?: number
  s6_pass_rate?: number
  entity_coverage?: number
  s4_entity_coverage?: number
  judged_passed?: number
  auditor_passed?: number
  judge_fails?: number
  auditor_fails?: number
}

export type PipelineEventType =
  | 'stage'
  | 'repair'
  | 'progress'
  | 'summary'
  | 'done'
  | 'error'

export interface PipelineEvent {
  type: PipelineEventType
  stage?: StageId | string
  node_id?: StageId | string
  status?: StageStatus
  engine?: string
  model?: string
  counts?: Record<string, number>
  preview?: string
  fail_reason?: string
  message?: string
  repairing?: boolean
  repair_path?: StageId[]
  repair_nodes?: StageId[]
  summary?: SummaryMetrics
  progress?: number
  inspector?: {
    preview?: string
    sample?: string[]
    fail_reason?: string
    counts?: Record<string, number>
    model?: string
    engine?: string
  }
  at?: number
  delay_ms?: number
  t?: number
}

export interface RunSnapshot {
  run_id: string
  mode?: string
  status?: AppMode | string
  stages?: Array<{
    id: StageId
    status: StageStatus
    model?: string
    counts?: Record<string, number>
  }>
  summary?: SummaryMetrics
  active_stage?: StageId
  repair_active?: boolean
  repair_nodes?: StageId[]
  repair_path?: StageId[]
  activity?: string
  inspector?: {
    node_id?: StageId
    status?: StageStatus
    model?: string
    engine?: string
    preview?: string
    sample?: string[]
    fail_reason?: string
    counts?: Record<string, number>
  }
  error?: string
}

export interface ReplayResponse {
  run_id: string
  events: PipelineEvent[]
  duration_ms?: number
}

export interface StageDef {
  id: StageId
  label: string
  stages: string
  callout: string
}
