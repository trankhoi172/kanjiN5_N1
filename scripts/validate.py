#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validation script for JLPT Kanji dataset (N5–N1).
Validates JSON syntax, schema compliance, field types, counts, and duplicates.
Runs with zero external dependencies (Python standard library only).
"""

import json
import os
import sys
from collections import Counter

EXPECTED_LEVELS = {
    "n5.json": {"level": "N5", "expected_count": 80},
    "n4.json": {"level": "N4", "expected_count": 167},
    "n3.json": {"level": "N3", "expected_count": 370},
    "n2.json": {"level": "N2", "expected_count": 368},
    "n1.json": {"level": "N1", "expected_count": 1235},
}

ALLOWED_KEYS = {
    "kanji",
    "level",
    "meanings",
    "onyomi",
    "kunyomi",
    "radical",
    "strokes",
    "examples",
}

EXAMPLE_KEYS = {"word", "reading", "meaning_vi", "meaning_en"}


def validate_entry(entry, expected_level, idx, filename):
    errors = []
    if not isinstance(entry, dict):
        return [f"{filename}[{idx}]: entry must be a JSON object, got {type(entry).__name__}"]

    extra_keys = set(entry.keys()) - ALLOWED_KEYS
    if extra_keys:
        errors.append(f"{filename}[{idx}]: unexpected keys {extra_keys}")

    # Required fields
    if "kanji" not in entry:
        errors.append(f"{filename}[{idx}]: missing required 'kanji' field")
    elif not isinstance(entry["kanji"], str) or len(entry["kanji"]) == 0:
        errors.append(f"{filename}[{idx}]: 'kanji' must be a non-empty string")

    if "level" not in entry:
        errors.append(f"{filename}[{idx}]: missing required 'level' field")
    elif entry["level"] != expected_level:
        errors.append(f"{filename}[{idx}]: 'level' expected '{expected_level}', got '{entry.get('level')}'")

    # Optional / nullable fields
    if "meanings" in entry and entry["meanings"] is not None:
        meanings = entry["meanings"]
        if not isinstance(meanings, dict):
            errors.append(f"{filename}[{idx}]: 'meanings' must be an object or null")
        else:
            meaning_extra = set(meanings.keys()) - {"vi", "en"}
            if meaning_extra:
                errors.append(f"{filename}[{idx}]: 'meanings' has unexpected keys {meaning_extra}")
            for lang in ["vi", "en"]:
                if lang in meanings and meanings[lang] is not None:
                    if not isinstance(meanings[lang], list) or not all(isinstance(m, str) for m in meanings[lang]):
                        errors.append(f"{filename}[{idx}]: 'meanings.{lang}' must be an array of strings")

    if "onyomi" in entry and entry["onyomi"] is not None:
        if not isinstance(entry["onyomi"], list) or not all(isinstance(o, str) for o in entry["onyomi"]):
            errors.append(f"{filename}[{idx}]: 'onyomi' must be an array of strings or null")

    if "kunyomi" in entry and entry["kunyomi"] is not None:
        if not isinstance(entry["kunyomi"], list) or not all(isinstance(k, str) for k in entry["kunyomi"]):
            errors.append(f"{filename}[{idx}]: 'kunyomi' must be an array of strings or null")

    if "radical" in entry and entry["radical"] is not None:
        if not isinstance(entry["radical"], str):
            errors.append(f"{filename}[{idx}]: 'radical' must be a string or null")

    if "strokes" in entry and entry["strokes"] is not None:
        if not isinstance(entry["strokes"], int) or entry["strokes"] < 1:
            errors.append(f"{filename}[{idx}]: 'strokes' must be a positive integer or null")

    if "examples" in entry and entry["examples"] is not None:
        examples = entry["examples"]
        if not isinstance(examples, list):
            errors.append(f"{filename}[{idx}]: 'examples' must be an array or null")
        else:
            for ex_idx, ex in enumerate(examples):
                if not isinstance(ex, dict):
                    errors.append(f"{filename}[{idx}].examples[{ex_idx}]: example must be an object")
                    continue
                ex_extra = set(ex.keys()) - EXAMPLE_KEYS
                if ex_extra:
                    errors.append(f"{filename}[{idx}].examples[{ex_idx}]: unexpected keys {ex_extra}")
                if "word" not in ex or not isinstance(ex["word"], str) or len(ex["word"]) == 0:
                    errors.append(f"{filename}[{idx}].examples[{ex_idx}]: 'word' must be a non-empty string")
                if "reading" not in ex or not isinstance(ex["reading"], str) or len(ex["reading"]) == 0:
                    errors.append(f"{filename}[{idx}].examples[{ex_idx}]: 'reading' must be a non-empty string")
                for m_key in ["meaning_vi", "meaning_en"]:
                    if m_key in ex and ex[m_key] is not None and not isinstance(ex[m_key], str):
                        errors.append(f"{filename}[{idx}].examples[{ex_idx}]: '{m_key}' must be a string or null")

    return errors


def validate_schema_file(schema_path):
    print(f"Checking schema file: {schema_path}")
    if not os.path.exists(schema_path):
        return [f"Schema file not found at {schema_path}"]
    try:
        with open(schema_path, "r", encoding="utf-8") as f:
            schema = json.load(f)
        if "$schema" not in schema:
            return ["Schema missing '$schema' definition"]
        print("  -> Schema is valid JSON and has $schema definition.")
        return []
    except Exception as e:
        return [f"Schema parsing error: {e}"]


def main():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    data_dir = os.path.join(root_dir, "data")
    schema_path = os.path.join(root_dir, "schema", "kanji.schema.json")

    print(f"Running Kanji Dataset Validator on {root_dir}")
    print("=" * 60)

    all_errors = []
    schema_errors = validate_schema_file(schema_path)
    all_errors.extend(schema_errors)

    level_kanji = {}
    total_kanji_count = 0

    print("\nValidating data files:")
    for filename, meta in EXPECTED_LEVELS.items():
        filepath = os.path.join(data_dir, filename)
        level_name = meta["level"]
        expected_count = meta["expected_count"]

        if not os.path.exists(filepath):
            all_errors.append(f"Missing file: {filepath}")
            continue

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            all_errors.append(f"JSON syntax error in {filename}: {e}")
            continue

        if not isinstance(data, list):
            all_errors.append(f"{filename}: Root must be a JSON array, got {type(data).__name__}")
            continue

        actual_count = len(data)
        total_kanji_count += actual_count

        kanji_chars = []
        file_errors = []

        for idx, entry in enumerate(data):
            entry_errors = validate_entry(entry, level_name, idx, filename)
            file_errors.extend(entry_errors)
            if isinstance(entry, dict) and "kanji" in entry:
                kanji_chars.append(entry["kanji"])

        # Check count
        count_status = "OK" if actual_count == expected_count else "MISMATCH"
        if actual_count != expected_count:
            file_errors.append(f"{filename}: expected {expected_count} items, found {actual_count}")

        # Check duplicates within file
        counter = Counter(kanji_chars)
        dups = [k for k, v in counter.items() if v > 1]
        if dups:
            file_errors.append(f"{filename}: duplicate characters found: {dups}")

        level_kanji[level_name] = kanji_chars

        print(f"  [{count_status}] {filename} ({level_name}): {actual_count}/{expected_count} items | Duplicates: {len(dups)}")
        if file_errors:
            for err in file_errors[:10]:
                print(f"      ERROR: {err}")
            if len(file_errors) > 10:
                print(f"      ... and {len(file_errors) - 10} more errors.")
            all_errors.extend(file_errors)

    # Cross-level overlap report
    print("\nChecking cross-level overlaps:")
    levels = list(EXPECTED_LEVELS.values())
    for i in range(len(levels)):
        for j in range(i + 1, len(levels)):
            l1 = levels[i]["level"]
            l2 = levels[j]["level"]
            if l1 in level_kanji and l2 in level_kanji:
                overlap = set(level_kanji[l1]).intersection(set(level_kanji[l2]))
                if overlap:
                    print(f"  [NOTE] Overlap between {l1} and {l2}: {len(overlap)} kanji -> {list(overlap)}")

    print("=" * 60)
    print(f"Total entries processed: {total_kanji_count}")
    if all_errors:
        print(f"FAILED: {len(all_errors)} errors detected.")
        sys.exit(1)
    else:
        print("SUCCESS: All datasets passed validation cleanly!")
        sys.exit(0)


if __name__ == "__main__":
    main()
