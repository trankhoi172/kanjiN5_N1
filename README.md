# kanjiN5_N1

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![JSON Schema](https://img.shields.io/badge/Schema-Draft%202020--12-green.svg)](schema/kanji.schema.json)
[![Kanji Count](https://img.shields.io/badge/Total%20Kanji-2%2C220-orange.svg)](#kanji-levels)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

An open-source, structured, and developer-friendly Japanese Kanji dataset covering **JLPT N5 to N1** (2,220 characters).

Designed for seamless integration into web applications, mobile apps, flashcard tools (Anki), NLP pipelines, and educational platforms.

---

## 1. Project Goals

- **Complete JLPT Coverage**: Categorized into 5 progressive levels from beginner (N5) to advanced (N1).
- **JSON-Native Architecture**: Standard JSON files with zero proprietary lock-in. Easy to consume across any programming language (JavaScript, TypeScript, Python, Go, Rust, Dart/Flutter, Swift, Kotlin, etc.).
- **Strict Data Quality & Schema**: Standardized with [JSON Schema Draft 2020-12](schema/kanji.schema.json) and validated via automated scripts.
- **Multilingual Support**: Ready for Vietnamese (`vi`) and English (`en`) meanings, with structure ready for future locale extensions.
- **Community-Driven**: Built for open-source collaboration, where developers and linguists can enrich readings, meanings, stroke counts, and vocabulary examples.

---

## 2. Kanji Levels & Distribution

| Level | Difficulty | Number of Kanji | Primary Target Audience | Data File |
| :--- | :--- | :---: | :--- | :--- |
| **N5** | Beginner | **80** | Introductory learners, basic numbers, days, directions | [`data/n5.json`](data/n5.json) |
| **N4** | Upper Beginner | **167** | Daily interactions, basic verbs, adjectives, locations | [`data/n4.json`](data/n4.json) |
| **N3** | Intermediate | **370** | Everyday conversational Japanese, common news topics | [`data/n3.json`](data/n3.json) |
| **N2** | Upper Intermediate | **368** | Business, social topics, media, general literature | [`data/n2.json`](data/n2.json) |
| **N1** | Advanced | **1,235** | High-level discourse, academic, specialized texts | [`data/n1.json`](data/n1.json) |
| **Total** | | **2,220** | | |

> [!NOTE]
> Since 2010, the official administering bodies of the JLPT (JEES / The Japan Foundation) do not publish official Kanji specifications. The counts and classifications in this library reflect the pedagogical curriculum established for this project. See [`docs/SOURCES.md`](docs/SOURCES.md) for details.

---

## 3. Repository Structure

```text
kanjiN5_N1/
├── README.md                  # Project overview, quickstart & documentation
├── LICENSE                    # MIT License
├── CONTRIBUTING.md            # Guidelines for contributing data and code
├── data/                      # Core dataset directory
│   ├── n5.json                # JLPT N5 Kanji (80 entries)
│   ├── n4.json                # JLPT N4 Kanji (167 entries)
│   ├── n3.json                # JLPT N3 Kanji (370 entries)
│   ├── n2.json                # JLPT N2 Kanji (368 entries)
│   └── n1.json                # JLPT N1 Kanji (1,235 entries)
├── schema/
│   └── kanji.schema.json      # JSON Schema (Draft 2020-12)
├── docs/
│   ├── DATA_FORMAT.md         # Detailed field specifications and examples
│   └── SOURCES.md             # Data provenance, attribution, and reference dictionaries
└── scripts/
    └── validate.py            # Zero-dependency Python validation script
```

---

## 4. Data Format

Each entry represents a single Kanji character object conforming to [`schema/kanji.schema.json`](schema/kanji.schema.json):

```json
{
  "kanji": "日",
  "level": "N5",
  "meanings": {
    "vi": ["ngày", "mặt trời"],
    "en": ["day", "sun"]
  },
  "onyomi": ["ニチ", "ジツ"],
  "kunyomi": ["ひ", "か"],
  "radical": null,
  "strokes": 4,
  "examples": [
    {
      "word": "日本",
      "reading": "にほん",
      "meaning_vi": "Nhật Bản",
      "meaning_en": "Japan"
    }
  ]
}
```

For entries whose readings and meanings are pending verification, fields default to empty arrays (`[]`) or `null`:

```json
{
  "kanji": "一",
  "level": "N5",
  "meanings": {
    "vi": [],
    "en": []
  },
  "onyomi": [],
  "kunyomi": [],
  "radical": null,
  "strokes": null,
  "examples": []
}
```

Detailed definitions for all fields can be found in [`docs/DATA_FORMAT.md`](docs/DATA_FORMAT.md).

---

## 5. Usage Examples

### JavaScript (Node.js)

```javascript
const fs = require("fs");

const kanji = JSON.parse(
  fs.readFileSync("./data/n5.json", "utf8")
);

console.log(kanji);
```

### TypeScript

```typescript
import * as fs from "fs";

interface Example {
  word: string;
  reading: string;
  meaning_vi?: string | null;
  meaning_en?: string | null;
}

interface KanjiEntry {
  kanji: string;
  level: "N5" | "N4" | "N3" | "N2" | "N1";
  meanings?: {
    vi?: string[];
    en?: string[];
  } | null;
  onyomi?: string[] | null;
  kunyomi?: string[] | null;
  radical?: string | null;
  strokes?: number | null;
  examples?: Example[] | null;
}

const n5Data: KanjiEntry[] = JSON.parse(
  fs.readFileSync("./data/n5.json", "utf-8")
);

console.log(`Loaded ${n5Data.length} N5 Kanji.`);
```

### Python

```python
import json

with open("data/n5.json", "r", encoding="utf-8") as f:
    n5_kanji = json.load(f)

# Find Kanji with stroke count <= 4
simple_kanji = [k["kanji"] for k in n5_kanji if k.get("strokes") and k["strokes"] <= 4]
print(f"Simple Kanji in N5: {simple_kanji}")
```

---

## 6. Validation

A built-in validation script ensures that every JSON file is syntactically valid, matches expected counts, has no duplicate characters per level, and adheres strictly to the schema:

```bash
python scripts/validate.py
```

*Note: Requires only standard Python 3 (no third-party dependencies).*

---

## 7. Contributing

Contributions are warmly welcomed! You can help by:
- Enriching missing Onyomi and Kunyomi readings.
- Adding Vietnamese (Hán-Việt, meaning) and English definitions.
- Providing high-frequency vocabulary examples.
- Correcting stroke counts and radicals.

Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) for full guidelines on making Pull Requests.

---

## 8. License

This repository is licensed under the [MIT License](LICENSE). You are free to use, modify, distribute, and incorporate this dataset into commercial and non-commercial projects.
