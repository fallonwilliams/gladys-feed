from datetime import UTC, datetime

from gladys_feed.global_energy_live import build_feed, compute_fragility, compute_vulnerability


def test_compute_fragility_stays_normalized() -> None:
    assert compute_fragility(grid_stability=0.68, reserve_margin=0.71) == 0.31


def test_compute_vulnerability_combines_risk_factors() -> None:
    assert compute_vulnerability(0.31, import_dependency=0.42, climate_exposure=0.33) == 0.35


def test_build_feed_returns_expected_shape() -> None:
    payload = build_feed(
        iso="la",
        edi=-0.8,
        grid_stability=0.68,
        reserve_margin=0.71,
        import_dependency=0.42,
        climate_exposure=0.33,
        actions_next24h=[2, 7, 13],
        bundle_reference="demo-firmware-v1",
        timestamp=datetime(2026, 4, 22, 15, 30, tzinfo=UTC),
    )

    assert payload["iso"] == "LA"
    assert payload["t"] == "2026-04-22T15:30:00Z"
    assert payload["fragility"] == 0.31
    assert payload["vulnerability"] == 0.35
    assert payload["actions_next24h"] == [2, 7, 13]
    assert len(payload["ota_hash"]) == 64
