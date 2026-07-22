import { STAGE_DEFS } from '../stages'
import type { StageId, StageStatus } from '../types'

interface PipelineGraphProps {
  statuses: Record<StageId, StageStatus>
  selected: StageId | null
  repairing: boolean
  repairPath: StageId[]
  onSelect: (id: StageId) => void
}

const NODE_W = 132
const NODE_H = 72
const GAP = 20
const PAD_X = 28
const PAD_Y = 56
const REPAIR_Y = 12

function nodeX(i: number) {
  return PAD_X + i * (NODE_W + GAP)
}

function nodeCenter(i: number) {
  return { x: nodeX(i) + NODE_W / 2, y: PAD_Y + NODE_H / 2 }
}

function indexOf(id: StageId) {
  return STAGE_DEFS.findIndex((s) => s.id === id)
}

export function PipelineGraph({
  statuses,
  selected,
  repairing,
  repairPath,
  onSelect,
}: PipelineGraphProps) {
  const width = PAD_X * 2 + STAGE_DEFS.length * NODE_W + (STAGE_DEFS.length - 1) * GAP
  const height = PAD_Y * 2 + NODE_H + 36
  const cy = PAD_Y + NODE_H / 2

  const path =
    repairPath.length >= 2
      ? repairPath
      : repairing
        ? (['judge', 'generate', 'translate', 'judge'] as StageId[])
        : []

  const repairSegments: { d: string; key: string }[] = []
  for (let i = 0; i < path.length - 1; i++) {
    const from = path[i]!
    const to = path[i + 1]!
    const fi = indexOf(from)
    const ti = indexOf(to)
    if (fi < 0 || ti < 0) continue
    const a = nodeCenter(fi)
    const b = nodeCenter(ti)
    const goingBack = ti < fi
    if (goingBack) {
      const midX = (a.x + b.x) / 2
      repairSegments.push({
        key: `${from}-${to}`,
        d: `M ${a.x} ${PAD_Y + 4} C ${a.x} ${REPAIR_Y}, ${midX} ${REPAIR_Y - 6}, ${b.x} ${PAD_Y + 4}`,
      })
    } else if (ti === fi + 1) {
      repairSegments.push({
        key: `${from}-${to}`,
        d: `M ${a.x + NODE_W / 2 - 8} ${a.y} L ${b.x - NODE_W / 2 + 8} ${b.y}`,
      })
    }
  }

  return (
    <section className="pipeline-wrap" aria-label="Pipeline stages">
      <svg
        className="pipeline-svg"
        viewBox={`0 0 ${width} ${height}`}
        role="img"
        aria-label="HackGrid pipeline graph"
      >
        <defs>
          <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <path d="M0,0 L10,3.5 L0,7 Z" fill="var(--line)" />
          </marker>
          <marker
            id="arrowhead-active"
            markerWidth="10"
            markerHeight="7"
            refX="9"
            refY="3.5"
            orient="auto"
          >
            <path d="M0,0 L10,3.5 L0,7 Z" fill="var(--accent)" />
          </marker>
          <marker id="arrowhead-done" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
            <path d="M0,0 L10,3.5 L0,7 Z" fill="var(--ok)" />
          </marker>
          <marker
            id="arrowhead-repair"
            markerWidth="10"
            markerHeight="7"
            refX="9"
            refY="3.5"
            orient="auto"
          >
            <path d="M0,0 L10,3.5 L0,7 Z" fill="var(--repair)" />
          </marker>
        </defs>

        {STAGE_DEFS.slice(0, -1).map((stage, i) => {
          const next = STAGE_DEFS[i + 1]!
          const x1 = nodeX(i) + NODE_W
          const x2 = nodeX(i + 1)
          const fromStatus = statuses[stage.id as StageId]
          const toStatus = statuses[next.id as StageId]
          const done = fromStatus === 'ok' || fromStatus === 'repairing'
          const active =
            fromStatus === 'ok' && (toStatus === 'running' || toStatus === 'repairing')
          const marker = active
            ? 'url(#arrowhead-active)'
            : done
              ? 'url(#arrowhead-done)'
              : 'url(#arrowhead)'

          return (
            <line
              key={`arrow-${stage.id}`}
              className="arrow-path"
              x1={x1 + 2}
              y1={cy}
              x2={x2 - 8}
              y2={cy}
              data-active={active ? 'true' : 'false'}
              data-done={done && !active ? 'true' : 'false'}
              markerEnd={marker}
            />
          )
        })}

        {repairSegments.map((seg) => (
          <path
            key={seg.key}
            className="repair-arc"
            data-visible="true"
            d={seg.d}
            markerEnd="url(#arrowhead-repair)"
          />
        ))}

        {repairing && path.length > 0 && (
          <text className="repair-label" data-visible="true" x={width / 2} y={REPAIR_Y - 2} textAnchor="middle">
            fail → repair loop
          </text>
        )}

        {STAGE_DEFS.map((stage, i) => {
          const x = nodeX(i)
          const y = PAD_Y
          const status = statuses[stage.id as StageId]
          return (
            <g
              key={stage.id}
              className="stage-node"
              data-status={status}
              data-selected={selected === stage.id ? 'true' : 'false'}
              onClick={() => onSelect(stage.id)}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  e.preventDefault()
                  onSelect(stage.id)
                }
              }}
              aria-label={`${stage.label} ${stage.stages}, ${status}`}
            >
              <rect className="node-body" x={x} y={y} width={NODE_W} height={NODE_H} rx={12} ry={12} />
              <text className="node-label" x={x + NODE_W / 2} y={y + 30}>
                {stage.label}
              </text>
              <text className="node-sub" x={x + NODE_W / 2} y={y + 50}>
                {stage.stages}
              </text>
              <text className="node-callout" x={x + NODE_W / 2} y={y + 64}>
                {stage.callout}
              </text>
            </g>
          )
        })}
      </svg>
    </section>
  )
}
