from dataclasses import asdict, dataclass
from datetime import datetime, timedelta
import json


@dataclass
class Phase:
    name: str
    duration_weeks: int
    overlap_with_prev_weeks: int = 0
    start: datetime | None = None
    end: datetime | None = None


class DesignAssist:
    """Build a fast-track schedule for an energy program clearance workflow."""

    TEMPLATE = [
        Phase("0. Intake", 2),
        Phase("1. Lean-permits sprint", 8),
        Phase("2. Parallel-grid lock-in", 6, overlap_with_prev_weeks=4),
        Phase("3. Commercial & offtake freeze", 4, overlap_with_prev_weeks=2),
        Phase("4. Bulk-supply reservation", 3, overlap_with_prev_weeks=1),
        Phase("5. Finance doc template drop", 2),
        Phase("6. Community benefit sign-off", 4),
        Phase("7. FID & NTP handshake", 1),
    ]

    def __init__(self, start_date: datetime):
        self.start_date = start_date
        self.phases = [Phase(**asdict(phase)) for phase in self.TEMPLATE]
        self._compute_timeline()

    def _compute_timeline(self) -> None:
        current_start = self.start_date
        for index, phase in enumerate(self.phases):
            if index > 0:
                current_start -= timedelta(weeks=phase.overlap_with_prev_weeks)
            phase.start = current_start
            phase.end = current_start + timedelta(weeks=phase.duration_weeks)
            current_start = phase.end

    def to_json(self, pretty: bool = True) -> str:
        payload = []
        for phase in self.phases:
            payload.append(
                {
                    **asdict(phase),
                    "start": phase.start.date().isoformat() if phase.start else None,
                    "end": phase.end.date().isoformat() if phase.end else None,
                }
            )
        return json.dumps(payload, indent=2 if pretty else None)
