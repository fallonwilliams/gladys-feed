# Global Energy Live

`Global Energy Live` is the compact telemetry payload described in the repository overview. This document turns that draft into a concrete repo artifact.

## Feed shape

Each feed is a small JSON document intended for low-bandwidth distribution:

```json
{
  "iso": "LA",
  "t": "2026-04-22T15:30:00Z",
  "edi": -0.8,
  "fragility": 0.31,
  "vulnerability": 0.35,
  "actions_next24h": [2, 7, 13],
  "ota_hash": "..."
}
```

## Repo integration

- `src/gladys_feed/global_energy_live.py` computes feed payloads.
- `src/gladys_feed/cli.py` generates a payload from the command line.
- `data/feeds/LA.json` is the checked-in example feed.
- `tests/test_global_energy_live.py` validates scoring and payload generation.
