"""JSON and CSV report export."""
import csv
import json
from pathlib import Path
from datetime import datetime, timezone


def _report_path(extension: str, output_dir: str = "reports") -> Path:
    directory = Path(output_dir)
    directory.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    return directory / f"shadowrecon_{stamp}.{extension}"


def save_json(data: dict, output_dir: str = "reports") -> Path:
    path = _report_path("json", output_dir)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    return path


def save_csv(results: list[dict], output_dir: str = "reports") -> Path:
    path = _report_path("csv", output_dir)
    fields = ["platform", "url", "status", "http_status", "checked_at_utc", "detail"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(results)
    return path
