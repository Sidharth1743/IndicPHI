import { Activity } from 'lucide-react'

export interface ActivityEntry {
  id: string
  time: string
  message: string
  tone?: 'info' | 'repair' | 'ok' | 'fail'
}

interface ActivityFeedProps {
  entries: ActivityEntry[]
}

export function ActivityFeed({ entries }: ActivityFeedProps) {
  return (
    <section className="activity-feed" aria-label="Live activity">
      <div className="activity-head">
        <Activity size={16} strokeWidth={1.75} aria-hidden />
        <h2>Activity</h2>
      </div>
      <ol className="activity-list">
        {entries.length === 0 ? (
          <li className="activity-empty">Waiting for pipeline events…</li>
        ) : (
          entries.map((e) => (
            <li key={e.id} className="activity-item" data-tone={e.tone ?? 'info'}>
              <time>{e.time}</time>
              <span>{e.message}</span>
            </li>
          ))
        )}
      </ol>
    </section>
  )
}
