
`Global Energy Live` is the example project for sustainability using compact synthetic data as described in the overview. 


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

## Repo 

- `src/gladys_feed/global_energy_live.py` computes feed ranking
- `src/gladys_feed/cli.py` generates a sustainability score
- `data/feeds/LA.json` is the example feed.
- `tests/test_global_energy_live.py` validates scoring
