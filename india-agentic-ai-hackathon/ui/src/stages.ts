import type { StageDef, StageId } from './types'

export const STAGE_DEFS: StageDef[] = [
  { id: 'seed', label: 'Seed', stages: 'S1–S3', callout: 'Nemotron Personas' },
  { id: 'generate', label: 'Generate', stages: 'S4', callout: 'NeMo Data Designer' },
  { id: 'translate', label: 'Translate', stages: 'S4b', callout: 'Tag-preserving Indic' },
  { id: 'judge', label: 'Judge', stages: 'S5', callout: 'Grok-4.3' },
  { id: 'audit', label: 'Audit', stages: 'S6', callout: 'Checksums / DICS' },
  { id: 'curate', label: 'Curate', stages: 'S7–S8', callout: 'NeMo Curator' },
  { id: 'export', label: 'Export', stages: 'S9–S10', callout: 'GLiNER + split' },
]

export const STAGE_IDS: StageId[] = STAGE_DEFS.map((s) => s.id)

export const DEFAULT_LANGUAGES = [
  { code: 'hi', name: 'Hindi' },
  { code: 'bn', name: 'Bengali' },
  { code: 'ta', name: 'Tamil' },
  { code: 'te', name: 'Telugu' },
  { code: 'mr', name: 'Marathi' },
  { code: 'gu', name: 'Gujarati' },
  { code: 'kn', name: 'Kannada' },
  { code: 'ml', name: 'Malayalam' },
  { code: 'pa', name: 'Punjabi' },
  { code: 'or', name: 'Odia' },
  { code: 'as', name: 'Assamese' },
  { code: 'en', name: 'English' },
]

export const DEFAULT_DEMO_LANGS = ['hi', 'bn', 'ta']

export const REPLAY_TARGET_MS = 28_000
