from lib.grammar_check import grammar_check
import pytest

def test_valid_check():
    assert grammar_check("Hello world.") == True
    assert grammar_check("Hello world!") == True
    assert grammar_check("Hello world?") == True   

def test_starts_capital_invalid_punctuation():
    assert grammar_check("HELLO WORLD,") == False
    assert grammar_check("HELLO WORLD:") == False

def test_starts_capital_no_punctuation():
    assert grammar_check("HELLO WORLD") == False

def test_starts_lowercase_valid_punctuation():
    assert grammar_check("hELLO WORLD!") == False

def test_invalid_input_raises_error():
    with pytest.raises(Exception) as e:
        grammar_check("")
    error_msg_empty_str = str(e.value)
    with pytest.raises(Exception) as e:
        grammar_check(5)
    error_msg_int = str(e.value)
    assert error_msg_empty_str == "Invalid input."
    assert error_msg_int == "Invalid input."