"""Thread-safe request-per-minute limiter for concurrent callers."""

from __future__ import annotations

import threading
import time


class RateLimiter:
    """Enforce a minimum spacing between ``acquire()`` calls across threads.

    Example: ``requests_per_minute=120`` → ≥0.5s between acquires.
    Prefer a value slightly under the account cap (e.g. 110 for Sarvam-105B
    Business at 120 RPM) so retries do not trip the hard limit.
    """

    def __init__(self, requests_per_minute: float | None) -> None:
        if requests_per_minute is not None and requests_per_minute <= 0:
            raise ValueError("requests_per_minute must be > 0 when set")
        self._min_interval_s = (
            None if requests_per_minute is None else 60.0 / float(requests_per_minute)
        )
        self._lock = threading.Lock()
        self._last_acquire_monotonic: float | None = None

    def acquire(self) -> None:
        if self._min_interval_s is None:
            return
        with self._lock:
            now = time.monotonic()
            if self._last_acquire_monotonic is not None:
                elapsed = now - self._last_acquire_monotonic
                wait = self._min_interval_s - elapsed
                if wait > 0:
                    time.sleep(wait)
            self._last_acquire_monotonic = time.monotonic()
