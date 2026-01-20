from lib.count_words import count_words
import pytest

def test_valid_input():
    foobar = 'this is four words'
    desired_result = 4
    assert count_words(foobar) == desired_result

def test_invalid_input():
    wrong = 1
    desired_result = "Invalid input."
    with pytest.raises(Exception) as e:
        count_words(wrong)
    error_msg = e.value
    assert str(error_msg) == desired_result


