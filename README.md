# gladys-feed

Glide-slope Lightweight Asynchronous Data Yield Stream

| Field             | Example                  | Comment                                      |
| ----------------- | ------------------------ | -------------------------------------------- |
| `iso`             | `"LA"`                   | ISO-3166 country code                        |
| `t`               | `"2026-04-10T06:00:00Z"` | Timestamp                                    |
| `edi`             | `-0.8`                   | Current Effective Depletion Index (%)        |
| `fragility`       | `0.31`                   | Rolling fragility score                      |
| `vulnerability`   | `0.62`                   | Rolling vulnerability score                  |
| `actions_next24h` | `[2,7,13]`               | IDs to execute next                          |
| `ota_hash`        | `"ec9c4e..."`            | SHA-256 of the next firmware bundle (if any) |


That’s it — always ≤ 1 kB.
