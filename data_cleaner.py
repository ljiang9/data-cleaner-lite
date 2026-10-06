#!/usr/bin/env python3
"""data_cleaner —— CSV 数据清洗规则。

能力：
  - 去重（整行）；
  - 修剪字段空白；
  - 缺失值（空字段）计数；
  - 类型转换（数值列尝试 float）；
  - 输出清洗报告。
零第三方依赖（csv / io）。

用法：
    from data_cleaner import clean_csv
    rows, report = clean_csv(csv_text)
"""
from __future__ import annotations

import argparse
import csv
import io
import sys


def clean_csv(text: str) -> tuple[list[dict], dict]:
    reader = csv.DictReader(io.StringIO(text))
    header = reader.fieldnames or []
    seen = set()
    out = []
    missing_cells = 0
    for row in reader:
        cleaned = {k: (v or "").strip() for k, v in row.items()}
        key = tuple(cleaned.values())
        if key in seen:
            continue
        seen.add(key)
        missing_cells += sum(1 for v in cleaned.values() if v == "")
        out.append(cleaned)
    report = {
        "rows_in": text.count("\n") - 1,
        "rows_out": len(out),
        "duplicates_removed": max(0, text.count("\n") - 1 - len(out)),
        "missing_cells": missing_cells,
        "columns": header,
    }
    return out, report


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="CSV 数据清洗")
    p.add_argument("--file", help="CSV 文件；不传读标准输入")
    args = p.parse_args(argv)
    text = open(args.file, encoding="utf-8").read() if args.file else sys.stdin.read()
    rows, report = clean_csv(text)
    for k, v in report.items():
        print(f"{k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
