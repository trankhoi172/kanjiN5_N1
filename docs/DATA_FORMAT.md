# Data Format Specification

This document provides a comprehensive specification of the data format and schema used across the `kanjiN5_N1` library.

---

## 1. Overview

All Kanji data in this repository is stored in standard **JSON** format, organized by JLPT level in the `data/` directory (`n5.json`, `n4.json`, `n3.json`, `n2.json`, `n1.json`).

Each file contains a JSON array of Kanji objects. Every Kanji object conforms to the project's JSON Schema defined in [`schema/kanji.schema.json`](../schema/kanji.schema.json).

### Design Principles

- **Predictable & Consistent**: Every entry follows an identical field structure across all levels.
- **Language-agnostic**: Easily imported into JavaScript, TypeScript, Python, Go, Rust, Java, or SQL databases.
- **Zero Hallucination**: Only verified, authoritative readings, meanings, and stroke counts are included. Missing or pending data is represented as `null` or empty arrays (`[]`), never fabricated.
- **Extensible**: Structured to support additional languages, frequency ranks, or stroke orders in future versions without breaking backward compatibility.

---

## 2. Field Specifications

| Field | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `kanji` | `string` | **Yes** | The single Kanji glyph. | `"日"` |
| `level` | `string` | **Yes** | JLPT level category. Must be one of: `"N5"`, `"N4"`, `"N3"`, `"N2"`, `"N1"`. | `"N5"` |
| `meanings` | `object` \| `null` | No | Multilingual meanings. | See below |
| `meanings.vi` | `array<string>` | No | Meanings in Vietnamese (including Hán-Việt & semantic definitions). | `["ngày", "mặt trời"]` |
| `meanings.en` | `array<string>` | No | Meanings in English. | `["day", "sun"]` |
| `onyomi` | `array<string>` \| `null` | No | On readings (on'yomi / 音読み), transcribed in **Katakana**. | `["ニチ", "ジツ"]` |
| `kunyomi` | `array<string>` \| `null` | No | Kun readings (kun'yomi / 訓読み), transcribed in **Hiragana**. | `["ひ", "か"]` |
| `radical` | `string` \| `null` | No | Kangxi radical (部首 / bộ thủ). | `"日"` or `null` |
| `strokes` | `integer` \| `null` | No | Total stroke count (positive integer $\ge 1$). | `4` |
| `examples` | `array<object>` \| `null` | No | Compound words or example vocabulary containing the Kanji. | See below |

### Example Entry (`examples[]`) Fields

| Field | Type | Required | Description | Example |
| :--- | :--- | :--- | :--- | :--- |
| `word` | `string` | **Yes** | The compound word / phrase in Japanese. | `"日本"` |
| `reading` | `string` | **Yes** | Kana reading (Hiragana / Katakana). | `"にほん"` |
| `meaning_vi` | `string` \| `null` | No | Vietnamese meaning of the word. | `"Nhật Bản"` |
| `meaning_en` | `string` \| `null` | No | English meaning of the word. | `"Japan"` |

---

## 3. Data Representation

### 3.1. Complete Entry (Enriched)

Here is a fully populated Kanji entry:

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

### 3.2. Initial / Skeleton Entry (Pending Enrichment)

In initial stages, characters that have not yet undergone manual or authoritative verification are kept in skeleton form:

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

> [!NOTE]
> Empty arrays (`[]`) are used for list fields (`meanings.vi`, `meanings.en`, `onyomi`, `kunyomi`, `examples`) to simplify client consumption (preventing null-pointer exceptions in frontend rendering). Nullable scalar fields (`radical`, `strokes`) default to `null`.

---

## 4. How to Enrich or Add Kanji Data

When contributing new details for an existing Kanji:

1. **Locate the target file**: Open the corresponding file in `data/` (`n5.json` to `n1.json`).
2. **Find the Kanji**: Search for `"kanji": "<target_char>"`.
3. **Fill in verified information**:
   - `meanings.vi`: Add standard Vietnamese definitions and common Hán-Việt translations.
   - `meanings.en`: Add standard English glosses.
   - `onyomi`: Add Katakana readings (e.g. `["カン", "ケン"]`).
   - `kunyomi`: Add Hiragana readings (e.g. `["み.る"]`). Use standard period notation `.` to delineate okurigana if applicable.
   - `strokes`: Set the verified stroke count (e.g. `8`).
   - `examples`: Add representative vocabulary items with accurate kana readings and translations.
4. **Validate**:
   Run the validation script to ensure JSON syntax and schema compliance:
   ```bash
   python scripts/validate.py
   ```

---

## 5. Naming and Formatting Rules

- **Character Encoding**: UTF-8 without Byte Order Mark (BOM).
- **Indentation**: 2 spaces (no tabs).
- **Line Endings**: LF (`\n`) or CRLF (consistent per git configuration).
- **Sorting**: Within each level file, the ordering reflects the foundational project classification. Entries should not be arbitrarily reordered or deleted.
- **Uniqueness**: Each Kanji must appear exactly once within its respective level dataset.
