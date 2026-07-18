"""Deterministic readability scorer for the readability skill.

Computes Flesch Reading Ease, Flesch-Kincaid Grade, Gunning Fog, and SMOG from
plain text using a stdlib-only syllable/sentence/word heuristic, so scores are
reproducible instead of estimated by eye. Word- and sentence-count based
metrics are consistent by construction (fed from the same tokenization).

Usage:
  readability_score.py <file>                 print metrics for one text
  readability_score.py -                      read the text from stdin
  readability_score.py --diff <before> <after>  print metrics for both, for
                                                  before/after revision checks
"""

import json
import re
import sys

AUX_VERBS = {"am", "is", "are", "was", "were", "be", "being", "been"}

ADVERB_SKIP = {
    "not", "never", "always", "often", "still", "also",
    "already", "recently", "rarely", "usually", "generally",
}

IRREGULAR_PARTICIPLES = {
    "done", "gone", "seen", "known", "given", "taken", "written", "spoken",
    "broken", "chosen", "driven", "eaten", "fallen", "forgotten", "hidden",
    "ridden", "risen", "shaken", "stolen", "sworn", "torn", "worn", "woken",
    "born", "begun", "drawn", "flown", "grown", "thrown", "shown", "held",
    "made", "said", "sold", "told", "found", "kept", "left", "meant", "paid",
    "stood", "understood", "lost", "sent", "spent", "built", "bought",
    "brought", "caught", "fought", "taught", "thought", "led", "read",
    "heard", "felt", "put", "set", "cut", "hit", "let", "bent", "burnt",
    "dealt", "hung", "laid", "lit", "sung", "swept", "wound",
}

INFLECTION_SUFFIXES = ("es", "ed", "ing")

_SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+")
_WORD_FIND = re.compile(r"[A-Za-z']+")
_NON_ALPHA = re.compile(r"[^a-z]")
_SYLLABLE_TRIM = re.compile(r"(?:[^laeiouy]es|ed|[^laeiouy]e)$")
_VOWEL_GROUPS = re.compile(r"[aeiouy]{1,2}")


def clean_word(word: str) -> str:
    return _NON_ALPHA.sub("", word.lower())


def count_syllables(word: str) -> int:
    core = clean_word(word)
    if not core:
        return 0
    if len(core) <= 3:
        return 1
    trimmed = _SYLLABLE_TRIM.sub("", core)
    trimmed = re.sub(r"^y", "", trimmed)
    return max(1, len(_VOWEL_GROUPS.findall(trimmed)))


def split_sentences(text: str) -> list:
    return [s.strip() for s in _SENTENCE_SPLIT.split(text.strip()) if s.strip()]


def split_words(sentence: str) -> list:
    return _WORD_FIND.findall(sentence)


def is_complex_word(word: str, is_sentence_start: bool) -> bool:
    core = clean_word(word)
    if count_syllables(core) < 3:
        return False
    if word[:1].isupper() and not is_sentence_start:
        return False
    for suffix in INFLECTION_SUFFIXES:
        if core.endswith(suffix) and count_syllables(core[: -len(suffix)]) < 3:
            return False
    return True


def sentence_is_passive(words: list) -> bool:
    lower = [w.lower() for w in words]
    for i, tok in enumerate(lower):
        if tok not in AUX_VERBS:
            continue
        for j in range(i + 1, min(i + 4, len(lower))):
            candidate = lower[j]
            if candidate in ADVERB_SKIP:
                continue
            if candidate.endswith("ed") or candidate in IRREGULAR_PARTICIPLES:
                return True
            break
    return False


def compute_metrics(text: str) -> dict:
    sentences = split_sentences(text)
    if not sentences:
        raise ValueError("no sentences found in text")

    all_words = []
    syllable_total = 0
    complex_count = 0
    polysyllable_count = 0
    passive_sentences = 0

    for sentence in sentences:
        words = split_words(sentence)
        if not words:
            continue
        if sentence_is_passive(words):
            passive_sentences += 1
        for idx, word in enumerate(words):
            all_words.append(word)
            syl = count_syllables(word)
            syllable_total += syl
            if syl >= 3:
                polysyllable_count += 1
            if is_complex_word(word, is_sentence_start=(idx == 0)):
                complex_count += 1

    word_count = len(all_words)
    sentence_count = len(sentences)
    if word_count == 0:
        raise ValueError("no words found in text")

    letters_total = sum(len(clean_word(w)) for w in all_words)
    avg_sentence_length = word_count / sentence_count
    avg_word_length = letters_total / word_count
    words_per_sentence = avg_sentence_length
    syllables_per_word = syllable_total / word_count

    flesch_reading_ease = 206.835 - 1.015 * words_per_sentence - 84.6 * syllables_per_word
    flesch_kincaid_grade = 0.39 * words_per_sentence + 11.8 * syllables_per_word - 15.59
    gunning_fog = 0.4 * (words_per_sentence + 100 * (complex_count / word_count))
    smog_index = 1.043 * ((polysyllable_count * (30 / sentence_count)) ** 0.5) + 3.1291

    return {
        "words": word_count,
        "sentences": sentence_count,
        "syllables": syllable_total,
        "avg_sentence_length": round(avg_sentence_length, 1),
        "avg_word_length": round(avg_word_length, 1),
        "complex_words": complex_count,
        "complex_word_pct": round(100 * complex_count / word_count, 1),
        "polysyllable_words": polysyllable_count,
        "passive_sentences": passive_sentences,
        "passive_pct": round(100 * passive_sentences / sentence_count, 1),
        "flesch_reading_ease": round(flesch_reading_ease, 1),
        "flesch_kincaid_grade": round(flesch_kincaid_grade, 1),
        "gunning_fog": round(gunning_fog, 1),
        "smog_index": round(smog_index, 1),
    }


USAGE = "usage: readability_score.py <file>|- | readability_score.py --diff <before> <after>"


def _read(path: str) -> str:
    if path == "-":
        return sys.stdin.read()
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        print(json.dumps({"error": f"file not found: {path}"}))
        sys.exit(1)


def _score(text: str) -> dict:
    try:
        return compute_metrics(text)
    except ValueError as e:
        print(json.dumps({"error": str(e)}))
        sys.exit(1)


def main(argv: list) -> None:
    if len(argv) < 1:
        print(USAGE, file=sys.stderr)
        sys.exit(2)
    if argv[0] == "--diff":
        if len(argv) != 3:
            print(USAGE, file=sys.stderr)
            sys.exit(2)
        before = _read(argv[1])
        after = _read(argv[2])
        print(json.dumps({"before": _score(before), "after": _score(after)}, indent=2))
    else:
        print(json.dumps(_score(_read(argv[0])), indent=2))


if __name__ == "__main__":
    main(sys.argv[1:])
