# Contributing to kanjiN5_N1

Thank you for your interest in contributing to **kanjiN5_N1**! We welcome contributions from developers, linguists, Japanese learners, and native speakers worldwide.

By contributing, you help create a clean, accessible, and structured open-source Kanji dataset for applications, study tools, and language research.

---

## 1. Code of Conduct & Contribution Philosophy

- **Accuracy Over Speed**: It is far better to leave a field empty or `null` than to enter speculative, machine-hallucinated, or incorrect data.
- **Respect Open Standards**: All data must conform strictly to [`schema/kanji.schema.json`](schema/kanji.schema.json).
- **Clear Attribution**: Always reference verified dictionaries or learning materials when supplying readings, meanings, or vocabulary.

---

## 2. Core Contribution Rules

To preserve data integrity, please adhere strictly to these rules:

1. **Do Not Add Out-of-Scope Kanji**: The dataset classifications across N5 through N1 represent the foundational scope of this project. Do not unilaterally add Kanji outside the existing level sets.
2. **Do Not Modify the JSON Structure Arbitrarily**: Any addition or modification must match the schema fields: `kanji`, `level`, `meanings` (`vi`, `en`), `onyomi`, `kunyomi`, `radical`, `strokes`, and `examples`. Do not add custom or ad-hoc top-level fields without discussing via an Issue first.
3. **Use Authoritative Sources**: Readings (Onyomi, Kunyomi), meanings (Vietnamese, English), stroke counts, and vocabulary examples must be derived from verified reference sources (see [`docs/SOURCES.md`](docs/SOURCES.md)).
4. **No Dubious or Copyright-Infringing Data**: Never import raw copyrighted dictionary exports that violate third-party licenses.

---

## 3. Contribution Workflow (Step-by-Step)

Follow these steps to submit your contributions:

### Step 1: Fork the Repository
Click the **Fork** button at the top right of the [GitHub repository page](https://github.com/trankhoi172/kanjiN5_N1) to create your own copy under your GitHub account.

### Step 2: Clone Your Fork
Clone your fork locally:
```bash
git clone https://github.com/<your-username>/kanjiN5_N1.git
cd kanjiN5_N1
```

### Step 3: Create a Descriptive Branch
Create a new git branch for your specific task:
```bash
git checkout -b enrich/n5-stroke-counts
# or
git checkout -b fix/n4-meanings
```

### Step 4: Add or Edit Data
Open the target JSON file in `data/` (`n5.json`, `n4.json`, `n3.json`, `n2.json`, `n1.json`) and edit the corresponding Kanji object according to [`docs/DATA_FORMAT.md`](docs/DATA_FORMAT.md).

For example, enriching `meanings` and `readings`:
```json
{
  "kanji": "学",
  "level": "N5",
  "meanings": {
    "vi": ["học", "học vấn", "khoa học"],
    "en": ["study", "learning", "science"]
  },
  "onyomi": ["ガク"],
  "kunyomi": ["まな.ぶ"],
  "radical": "子",
  "strokes": 8,
  "examples": [
    {
      "word": "学生",
      "reading": "がくせい",
      "meaning_vi": "học sinh, sinh viên",
      "meaning_en": "student"
    }
  ]
}
```

### Step 5: Validate Your Changes
Ensure all JSON files are formatted correctly, syntactically valid, and compliant with the schema:
```bash
python scripts/validate.py
```
> [!IMPORTANT]
> All automated validation checks must pass (`SUCCESS: All datasets passed validation cleanly!`) before creating a Pull Request.

### Step 6: Commit and Push
Commit your changes with a clear, concise commit message:
```bash
git add data/n5.json
git commit -m "feat(n5): add meanings and readings for 学"
git push origin enrich/n5-stroke-counts
```

### Step 7: Open a Pull Request (PR)
1. Navigate to the original [kanjiN5_N1 repository](https://github.com/trankhoi172/kanjiN5_N1).
2. Click **New Pull Request** and select your branch.
3. Fill in the PR description:
   - What was added / updated.
   - The reference sources used (e.g., KANJIDIC2, Từ điển Hán Việt).
   - Confirmation that `python scripts/validate.py` passed.

---

## 4. Reporting Issues & Proposing Enhancements

If you encounter a typo, inaccurate reading, or want to suggest structural improvements:
- Open an Issue in the [Issues tab](https://github.com/trankhoi172/kanjiN5_N1/issues).
- Provide evidence or source references when disputing a reading or definition.
