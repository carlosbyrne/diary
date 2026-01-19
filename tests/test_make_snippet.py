from lib.make_snippet import make_snippet
import pytest

def test_valid_input_more_than_5():
    foobar = "foobar"
    desired_result = "fooba..."
    assert make_snippet(foobar) == desired_result

def test_valid_input_5_or_less():
    fooba = "fooba"
    desired_result = "fooba"
    assert make_snippet(fooba) == desired_result

def test_invalid_input():
    wrong = 1
    desired_result = "Invalid input."
    with pytest.raises(Exception) as e:
        make_snippet(wrong)
    error_msg = e.value
    assert str(error_msg) == desired_result