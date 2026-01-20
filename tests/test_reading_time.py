from lib.reading_time import estimate_reading_time
import pytest

def test_200_words():
    words = "word " * 200
    assert estimate_reading_time(words) == 1.0

def test_400_words():
    words = "word " * 400
    assert estimate_reading_time(words) == 2.0

def test_300_words():
    words = "word " * 300
    assert estimate_reading_time(words) == 1.5

def test_100_words():
    words = "word " * 100
    assert estimate_reading_time(words) == 0.5

def test_empty_string_raises_error():
    with pytest.raises(Exception) as e:
        estimate_reading_time("")
    error_msg = str(e.value)
    assert error_msg == "Invalid input."

def test_non_string_raises_error():
    with pytest.raises(Exception) as e:
        estimate_reading_time(5)
    error_msg = str(e.value)
    assert error_msg == "Invalid input."