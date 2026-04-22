# gladys-feed

`gladys-feed` now contains a concrete `Global Energy Live` implementation instead of loose draft snippets. The repository packages a compact feed generator, an example feed artifact, supporting planning modules, and test coverage.

## Global Energy Live

The feed is intended to stay small enough for low-bandwidth distribution while still exposing the core operational state for a country or region:

| Field | Example | Comment |
| --- | --- | --- |
| `iso` | `"LA"` | ISO-3166 country code |
| `t` | `"2026-04-22T15:30:00Z"` | Timestamp |
| `edi` | `-0.8` | Effective Depletion Index |
| `fragility` | `0.31` | Grid resilience stress score |
| `vulnerability` | `0.35` | Combined exposure and dependency risk |
| `actions_next24h` | `[2, 7, 13]` | Action IDs to execute next |
| `ota_hash` | `"4f3988..."` | SHA-256 of the next bundle reference |

## Repo layout

- `src/gladys_feed/`: package code for feed generation, call signs, and planning support.
- `data/feeds/`: checked-in example feed payloads.
- `data/feeds/countries.json`: registry used by the multi-country dashboard selector.
- `dashboard/`: static operator dashboard for the sample feed.
- `docs/`: implementation notes and migrated draft context.
- `tests/`: automated coverage for feed scoring and payload generation.

## Quick start

```powershell
python -m pip install -e .[dev]
python -m gladys_feed.cli `
  --iso LA `
  --edi -0.8 `
  --grid-stability 0.68 `
  --reserve-margin 0.71 `
  --import-dependency 0.42 `
  --climate-exposure 0.33 `
  --bundle-reference "demo-firmware-v1" `
  --action 2 `
  --action 7 `
  --action 13
pytest
```

Open `dashboard/index.html` in a browser to view the static dashboard, or serve the repo locally if your browser blocks local `fetch()` calls. The dashboard now switches between multiple checked-in country feeds from `data/feeds/`.

## Notes

The original root-level draft files were normalized into package modules and documentation so the repo is importable, testable, and ready for further integration work.
