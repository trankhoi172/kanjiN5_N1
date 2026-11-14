# Data Sources and Attribution

This document describes the provenance of the Kanji datasets in `kanjiN5_N1`, clarifies data licensing, and provides reference guidance for future contributions.

---

## 1. Important Disclaimer on JLPT Classifications

The Japanese-Language Proficiency Test (JLPT) is administered by Japan Educational Exchanges and Services (JEES) and The Japan Foundation. 

Since the JLPT reform in 2010, the official administering bodies **no longer publish official lists** of required vocabulary or Kanji for levels N5 through N1. Consequently:
- The Kanji classifications (N5: 80, N4: 167, N3: 370, N2: 368, N1: 1235; total: 2,220) contained in this repository are based on community and pedagogical consensus commonly used in Japanese language education.
- This library makes **no claim** of official affiliation with or endorsement by JEES, The Japan Foundation, or the JLPT administrative committee.

---

## 2. Current Dataset Provenance

### 2.1. Initial Kanji Character Lists (N5–N1)
- **Status**: Included in repository (`data/n5.json` through `data/n1.json`).
- **Nature**: Curated list of 2,220 characters grouped into five JLPT levels:
  - N5: 80 Kanji
  - N4: 167 Kanji
  - N3: 370 Kanji
  - N2: 368 Kanji
  - N1: 1,235 Kanji
- **Note on Character Forms**: The source set preserves historical and pedagogical selections, including standard Jōyō Kanji, Jinmeiyō Kanji, and certain simplified or variant glyphs present in popular reference lists. In accordance with the project's data integrity rules, all glyphs are preserved exactly as imported without unauthorized substitution.

### 2.2. Sample Data
- The reference data for `日` in `data/n5.json` was authored and verified as a baseline template directly by project maintainers.

---

## 3. Recommended External Reference Sources for Community Contributions

To enrich the library with verified readings (Onyomi, Kunyomi), meanings (Vietnamese, English), stroke counts, and vocabulary examples, contributors are advised to consult the following authoritative and open-access resources:

### 3.1. KANJIDIC2 & JMdict
- **Maintained by**: The Electronic Dictionary Research and Development Group (EDRDG), founded by Jim Breen.
- **Scope**: Comprehensive digital Japanese-English dictionary and Kanji dictionary database.
- **License**: [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/).
- **URL**: [https://www.edrdg.org/](https://www.edrdg.org/)

### 3.2. Jōyō Kanji & Jinmeiyō Kanji Standards
- **Maintained by**: Agency for Cultural Affairs, Ministry of Education, Culture, Sports, Science and Technology (MEXT), Japan.
- **Scope**: Official list of 2,136 regular-use characters (常用漢字表) and name-use characters (人名用漢字).
- **Status**: Official governmental standard (public regulatory text).
- **URL**: [https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/kanjihyo/](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kijun/naikaku/kanjihyo/)

### 3.3. KanjiVG
- **Created by**: Ulrich Apel and contributors.
- **Scope**: Vector graphics and stroke order / stroke count data for Japanese characters.
- **License**: [Creative Commons Attribution-ShareAlike 3.0 Unported (CC BY-SA 3.0)](https://creativecommons.org/licenses/by-sa/3.0/).
- **URL**: [https://kanjivg.tagaini.net/](https://kanjivg.tagaini.net/)

### 3.4. Sino-Vietnamese (Hán-Việt) & Vietnamese Glosses
- **Recommended References**:
  - *Từ điển Hán Việt* (Đào Duy Anh).
  - *Hán Việt Từ Điển Trích Dẫn* (Viện Việt Học).
  - Standardized modern textbooks (Minna no Nihongo Kanji, Kanji Look and Learn).

---

## 4. Attribution & Data Integrity Policy

1. **Verify Before Adding**: Never submit speculative, AI-hallucinated, or unverified readings/meanings. If a reading or stroke count is uncertain, leave it as `null` or empty array.
2. **Respect Copyright**: Do not scrape or reproduce proprietary copyrighted dictionary entries wholesale without appropriate licensing permission.
3. **Document Additions**: When submitting major batch enrichments via Pull Request, specify the reference dictionary or source used in the PR description.
