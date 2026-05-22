# gladys-feed

`gladys-feed` now contains a concrete `Global Energy Live` for sustainability goals 2056. 

## Global Sustainability Live

The repository packages a compact feed for researching environmental changes for sustainability. 

| Field | Example | Comment |
| --- | --- | --- |
| `iso` | `"LA"` | Example of Code for Locations Using UNNESCO locations for World Historical Sites|
| `t` | `"2026-04-22T15:30:00Z"` | Timestamp |
| `edi` | `-0.8` | Example Depletion Index |
| `fragility` | `0.31` | Sustainabiliy Capacity Rankings|
| `vulnerability` | `0.35` |Sustainability Risk |
| `actions_next24h` | `[2, 7, 13]` | Next Example  |
| `ota_hash` | `"4f3988..."` | SHA-256 of the next bundle reference |

## Repo layout

- `src/gladys_feed/`: package code for planning support.
- `data/feeds/`: checked-in example
- `data/feeds/countries.json`: registry dashboard selector.
- `dashboard/`: static operator dashboard for the sample .
- `docs/`: notes and migrated draft context.
- `tests/`:  coverage scoring for ranking sustainability metrics 

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

Open `dashboard/index.html` in a browser to view the static dashboard, or serve the repo locally if your browser blocks local `fetch()` calls.

## Notes

The package modules and documentation are compact to be ready for further research and sustainability development work.
