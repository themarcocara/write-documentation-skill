import json
import pathlib
import subprocess
import sys

from scripts.readability_score import (
    compute_metrics,
    count_syllables,
    is_complex_word,
    sentence_is_passive,
    split_sentences,
)

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCRIPT = REPO_ROOT / "scripts" / "readability_score.py"


def _run_cli(*args, input=None):
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=str(REPO_ROOT),
        input=input,
        capture_output=True,
        text=True,
    )


def test_count_syllables_simple_words():
    assert count_syllables("cat") == 1
    assert count_syllables("happy") == 2
    assert count_syllables("elephant") == 3


def test_count_syllables_silent_e():
    assert count_syllables("make") == 1
    assert count_syllables("hope") == 1


def test_split_sentences_basic():
    assert split_sentences("One. Two! Three?") == ["One.", "Two!", "Three?"]


def test_is_complex_word_requires_three_syllables():
    assert is_complex_word("beautiful", is_sentence_start=False) is True
    assert is_complex_word("cat", is_sentence_start=False) is False


def test_is_complex_word_excludes_proper_nouns_mid_sentence():
    # "Antarctica" mid-sentence looks like a proper noun and is excluded
    assert is_complex_word("Antarctica", is_sentence_start=False) is False
    # the same word at a sentence start is judged on syllables alone
    assert is_complex_word("Antarctica", is_sentence_start=True) is True


def test_is_complex_word_excludes_inflected_shorter_words():
    # "governed" is only 3 syllables via "-ed"; the root "govern" is 2
    assert is_complex_word("governed", is_sentence_start=False) is False


def test_sentence_is_passive_detects_be_plus_participle():
    assert sentence_is_passive(["The", "cake", "was", "eaten"]) is True
    assert sentence_is_passive(["The", "report", "was", "written", "by", "her"]) is True


def test_sentence_is_passive_false_for_active_voice():
    assert sentence_is_passive(["She", "ate", "the", "cake"]) is False


def test_compute_metrics_returns_expected_keys():
    metrics = compute_metrics("The cat sat on the mat. It was warm.")
    assert set(metrics) == {
        "words", "sentences", "syllables", "avg_sentence_length",
        "avg_word_length", "complex_words", "complex_word_pct",
        "polysyllable_words", "passive_sentences", "passive_pct",
        "flesch_reading_ease", "flesch_kincaid_grade", "gunning_fog",
        "smog_index",
    }
    assert metrics["words"] == 9
    assert metrics["sentences"] == 2


def test_compute_metrics_empty_text_raises():
    try:
        compute_metrics("")
        assert False, "expected ValueError"
    except ValueError:
        pass


def test_cli_no_args_exits_2():
    assert _run_cli().returncode == 2


def test_cli_missing_file_exits_1_with_json_error():
    result = _run_cli("does_not_exist_12345.txt")
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert "error" in payload


def test_cli_stdin_mode(tmp_path):
    result = _run_cli("-", input="The cat sat on the mat. It was warm.")
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["words"] == 9


def test_cli_single_file_success(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("The cat sat on the mat. It was warm.", encoding="utf-8")
    result = _run_cli(str(f))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["sentences"] == 2


def test_cli_diff_mode(tmp_path):
    before = tmp_path / "before.txt"
    after = tmp_path / "after.txt"
    before.write_text("The company was founded by a group of investors.", encoding="utf-8")
    after.write_text("A group of investors founded the company.", encoding="utf-8")
    result = _run_cli("--diff", str(before), str(after))
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert "before" in payload and "after" in payload
    assert payload["before"]["passive_sentences"] == 1
    assert payload["after"]["passive_sentences"] == 0


def test_cli_diff_wrong_arg_count_exits_2():
    result = _run_cli("--diff", str(SCRIPT))
    assert result.returncode == 2
