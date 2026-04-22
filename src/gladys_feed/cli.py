from __future__ import annotations

import argparse
import json

from .global_energy_live import build_feed


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Generate a Global Energy Live feed document.")
    parser.add_argument("--iso", required=True)
    parser.add_argument("--edi", type=float, required=True)
    parser.add_argument("--grid-stability", type=float, required=True)
    parser.add_argument("--reserve-margin", type=float, required=True)
    parser.add_argument("--import-dependency", type=float, required=True)
    parser.add_argument("--climate-exposure", type=float, required=True)
    parser.add_argument("--bundle-reference", required=True)
    parser.add_argument("--action", type=int, action="append", dest="actions_next24h", default=[])
    return parser


def main() -> None:
    args = build_parser().parse_args()
    payload = build_feed(
        iso=args.iso,
        edi=args.edi,
        grid_stability=args.grid_stability,
        reserve_margin=args.reserve_margin,
        import_dependency=args.import_dependency,
        climate_exposure=args.climate_exposure,
        actions_next24h=args.actions_next24h,
        bundle_reference=args.bundle_reference,
    )
    print(json.dumps(payload, indent=2))


if __name__ == "__main__":
    main()
