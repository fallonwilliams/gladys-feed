from __future__ import annotations

from datetime import UTC, datetime
from hashlib import sha256


def _clamp(value: float, minimum: float = 0.0, maximum: float = 1.0) -> float:
    return max(minimum, min(maximum, value))


def compute_fragility(grid_stability: float, reserve_margin: float) -> float:
    fragility = (1.0 - grid_stability) * 0.65 + (1.0 - reserve_margin) * 0.35
    return round(_clamp(fragility), 2)


def compute_vulnerability(
    fragility: float, import_dependency: float, climate_exposure: float
) -> float:
    vulnerability = fragility * 0.5 + _clamp(import_dependency) * 0.3 + _clamp(climate_exposure) * 0.2
    return round(_clamp(vulnerability), 2)


def build_feed(
    iso: str,
    edi: float,
    grid_stability: float,
    reserve_margin: float,
    import_dependency: float,
    climate_exposure: float,
    actions_next24h: list[int],
    bundle_reference: str,
    timestamp: datetime | None = None,
) -> dict[str, object]:
    observed_at = timestamp.astimezone(UTC) if timestamp else datetime.now(UTC)
    fragility = compute_fragility(grid_stability, reserve_margin)
    vulnerability = compute_vulnerability(fragility, import_dependency, climate_exposure)
    ota_hash = sha256(bundle_reference.encode("utf-8")).hexdigest()
    return {
        "iso": iso.upper(),
        "t": observed_at.isoformat().replace("+00:00", "Z"),
        "edi": round(edi, 2),
        "fragility": fragility,
        "vulnerability": vulnerability,
        "actions_next24h": actions_next24h,
        "ota_hash": ota_hash,
    }
