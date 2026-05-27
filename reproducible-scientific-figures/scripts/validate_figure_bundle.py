#!/usr/bin/env python3
"""Read-only validator for reproducible scientific figure bundles.

The script validates a small JSON figure spec with standard-library Python.
If a YAML spec is provided and PyYAML is installed, YAML is supported too.
It checks required metadata and referenced file existence only; it does not
verify scientific correctness or render figures.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_FIELDS = [
    "figure_id",
    "purpose",
    "figure_ready_data",
    "plot_code",
    "outputs",
]


def load_spec(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    suffix = path.suffix.lower()
    if suffix == ".json":
        data = json.loads(text)
    elif suffix in {".yaml", ".yml"}:
        try:
            import yaml  # type: ignore
        except Exception as exc:  # pragma: no cover - depends on environment
            raise SystemExit(
                "YAML spec requires PyYAML. Use JSON or install PyYAML."
            ) from exc
        data = yaml.safe_load(text)
    else:
        raise SystemExit("Spec must be .json, .yaml, or .yml")
    if not isinstance(data, dict):
        raise SystemExit("Spec root must be an object")
    return data


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def resolve(base: Path, value: Any) -> Path | None:
    if not isinstance(value, str) or not value.strip():
        return None
    p = Path(value)
    if not p.is_absolute():
        p = base / p
    return p


def check_path(label: str, base: Path, value: Any, required: bool, messages: list[str]) -> None:
    path = resolve(base, value)
    if path is None:
        if required:
            messages.append(f"FAIL missing required path: {label}")
        return
    if path.exists():
        messages.append(f"OK {label}: {path}")
    else:
        level = "FAIL" if required else "WARN"
        messages.append(f"{level} missing {label}: {path}")


def validate(spec_path: Path) -> int:
    spec = load_spec(spec_path)
    base = spec_path.parent
    messages: list[str] = []
    fail = False

    for field in REQUIRED_FIELDS:
        if field not in spec or spec[field] in (None, "", []):
            messages.append(f"FAIL missing required field: {field}")
            fail = True
        else:
            messages.append(f"OK field: {field}")

    for item in as_list(spec.get("input_data") or spec.get("source_data")):
        check_path("input_data", base, item, required=False, messages=messages)

    check_path("figure_ready_data", base, spec.get("figure_ready_data"), True, messages)
    check_path("plot_code", base, spec.get("plot_code"), True, messages)

    outputs = spec.get("outputs", {})
    if isinstance(outputs, dict):
        if "svg" not in outputs:
            messages.append("FAIL outputs.svg is required as the editable master")
            fail = True
        for name, value in outputs.items():
            check_path(f"outputs.{name}", base, value, required=(name == "svg"), messages=messages)
    else:
        messages.append("FAIL outputs must be an object")
        fail = True

    for line in messages:
        print(line)
        if line.startswith("FAIL"):
            fail = True

    return 1 if fail else 0


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("spec", help="Path to figure_spec.json/yaml")
    args = parser.parse_args()
    return validate(Path(args.spec).resolve())


if __name__ == "__main__":
    sys.exit(main())
