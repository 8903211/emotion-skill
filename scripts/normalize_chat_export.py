#!/usr/bin/env python3
"""Normalize authorized chat exports to JSONL.

This script does not decrypt or access accounts. It only reads files the user
already exported and writes a simplified JSONL stream for analysis.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
from pathlib import Path
from typing import Any, Iterable


SUPPORTED_SUFFIXES = {".json", ".jsonl", ".csv", ".txt"}


def iter_input_files(path: Path) -> Iterable[Path]:
    if path.is_file():
        yield path
        return
    for child in sorted(path.rglob("*")):
        if child.is_file() and child.suffix.lower() in SUPPORTED_SUFFIXES:
            yield child


def coerce_timestamp(value: Any) -> str:
    if value is None:
        return ""
    return str(value).strip()


def normalize_record(record: dict[str, Any], source: Path, index: int, chat: str = "") -> dict[str, Any]:
    timestamp = (
        record.get("timestamp")
        or record.get("time")
        or record.get("datetime")
        or record.get("date")
        or record.get("CreateTime")
        or record.get("create_time")
        or ""
    )
    sender = (
        record.get("sender")
        or record.get("from")
        or record.get("speaker")
        or record.get("talker")
        or record.get("is_sender")
        or record.get("StrTalker")
        or ""
    )
    content = (
        record.get("content")
        or record.get("text")
        or record.get("message")
        or record.get("StrContent")
        or record.get("msg")
        or ""
    )
    msg_type = record.get("type") or record.get("msg_type") or record.get("Type") or "text"
    return {
        "timestamp": coerce_timestamp(timestamp),
        "sender": str(sender).strip(),
        "type": str(msg_type).strip() if msg_type is not None else "text",
        "content": str(content).strip(),
        "chat": chat,
        "source_file": str(source),
        "raw_index": index,
    }


def records_from_json(path: Path) -> Iterable[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    chat = ""
    if isinstance(data, dict):
        chat = str(data.get("chat") or data.get("contact_remark") or data.get("contact_nick_name") or "")
        messages = data.get("messages")
        if isinstance(messages, list):
            for index, record in enumerate(messages):
                if isinstance(record, dict):
                    yield normalize_record(record, path, index, chat)
            return
        if all(k in data for k in ("timestamp", "content")) or any(k in data for k in ("StrContent", "message")):
            yield normalize_record(data, path, 0, chat)
            return
        for key, value in data.items():
            if isinstance(value, list):
                for index, record in enumerate(value):
                    if isinstance(record, dict):
                        yield normalize_record(record, path, index, str(key))
    elif isinstance(data, list):
        for index, record in enumerate(data):
            if isinstance(record, dict):
                yield normalize_record(record, path, index, chat)


def records_from_jsonl(path: Path) -> Iterable[dict[str, Any]]:
    for index, line in enumerate(path.read_text(encoding="utf-8-sig").splitlines()):
        line = line.strip()
        if not line:
            continue
        record = json.loads(line)
        if isinstance(record, dict):
            yield normalize_record(record, path, index)


def records_from_csv(path: Path) -> Iterable[dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        for index, record in enumerate(reader):
            yield normalize_record(dict(record), path, index)


TXT_LINE_RE = re.compile(
    r"^(?:(?P<timestamp>\d{4}[-/]\d{1,2}[-/]\d{1,2}[ T]\d{1,2}:\d{2}(?::\d{2})?)\s+)?"
    r"(?:(?P<sender>[^:：]{1,40})[:：]\s*)?"
    r"(?P<content>.*)$"
)


def records_from_txt(path: Path) -> Iterable[dict[str, Any]]:
    for index, line in enumerate(path.read_text(encoding="utf-8-sig", errors="replace").splitlines()):
        if not line.strip():
            continue
        match = TXT_LINE_RE.match(line)
        if not match:
            continue
        yield {
            "timestamp": (match.group("timestamp") or "").strip(),
            "sender": (match.group("sender") or "").strip(),
            "type": "text",
            "content": (match.group("content") or "").strip(),
            "chat": "",
            "source_file": str(path),
            "raw_index": index,
        }


def read_records(path: Path) -> Iterable[dict[str, Any]]:
    suffix = path.suffix.lower()
    if suffix == ".json":
        yield from records_from_json(path)
    elif suffix == ".jsonl":
        yield from records_from_jsonl(path)
    elif suffix == ".csv":
        yield from records_from_csv(path)
    elif suffix == ".txt":
        yield from records_from_txt(path)


def main() -> int:
    parser = argparse.ArgumentParser(description="Normalize authorized chat exports to JSONL.")
    parser.add_argument("input", help="Input file or directory")
    parser.add_argument("--output", "-o", required=True, help="Output JSONL path")
    parser.add_argument("--drop-empty", action="store_true", help="Skip records with empty content")
    args = parser.parse_args()

    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    count = 0
    files = list(iter_input_files(input_path))
    with output_path.open("w", encoding="utf-8", newline="\n") as out:
        for file_path in files:
            try:
                for record in read_records(file_path):
                    if args.drop_empty and not record.get("content"):
                        continue
                    out.write(json.dumps(record, ensure_ascii=False) + "\n")
                    count += 1
            except Exception as exc:  # keep processing other files
                error_record = {
                    "timestamp": "",
                    "sender": "system",
                    "type": "error",
                    "content": f"failed to parse: {exc}",
                    "chat": "",
                    "source_file": str(file_path),
                    "raw_index": -1,
                }
                out.write(json.dumps(error_record, ensure_ascii=False) + "\n")

    print(json.dumps({"files": len(files), "records": count, "output": str(output_path)}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
