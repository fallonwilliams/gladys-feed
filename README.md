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


| Cloud                         | Free tier used              | Daily cost | Notes                                                     |
| ----------------------------- | --------------------------- | ---------- | --------------------------------------------------------- |
| **GitHub Pages**              | 1 GB storage, unlimited GET | $0         | Each country’s feed lives as `iso.json` in a public repo. |
| **Cloudflare Workers KV**     | 100 k reads/day             | $0         | Doubles as global CDN; worker updates the JSON.           |
| **SendGrid Essentials Trial** | 100 emails/day              | $0         | Fallback “email feed” if HTTP fails.                      |
| **Twilio Trial**              | 100 SMS/month               | $0         | Last-ditch SMS containing `edi` and action count.         |


Because the JSON is static until the next 30-min refresh, it qualifies for permanent caching on the free tiers.

# one-liner cron every 30 min
curl -s https://gladys-feed.pages.dev/LA.json -o /var/gladys/current.json

# fallback handler snippet
sms_data=$(gammu getallsms | grep -A1 "GLADYS" | tail -1)
# SMS example: 2026-04-10T06:00Z EDI=-0.8 ACT=3
