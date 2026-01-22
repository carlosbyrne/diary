from lib.diary import DiaryEntry
import pytest

def test_initalisation():
    diary = DiaryEntry('foo', 'bar')
    assert isinstance(diary, DiaryEntry)
    assert diary.title == 'foo'
    assert diary.contents == 'bar'

def test_format_method():
    diary = DiaryEntry('foo', 'bar')
    desired_result = "foo: bar"
    result = diary.format()
    assert result == desired_result

def test_count_words():
    words = "foobar " * 200
    diary = DiaryEntry('foo', words)
    desired_result = 200
    result = diary.count_words()
    assert result == desired_result

def test_reading_time_one_minute():
    words = "foobar " * 200
    diary = DiaryEntry('foo', words)
    desired_result = 1.0
    result = diary.reading_time(200)
    assert result == desired_result

def test_reading_time_half_minute():
    words = "foobar " * 100
    diary = DiaryEntry('foo', words)
    desired_result = 0.5
    result = diary.reading_time(200)
    assert result == desired_result

def test_reading_time_half_minute_100_wpm():
    words = "foobar " * 50
    diary = DiaryEntry('foo', words)
    desired_result = 0.5
    result = diary.reading_time(100)
    assert result == desired_result

def test_reading_chunk_20_words_one_call():
    words = "foobar " * 100
    diary = DiaryEntry('foo', words)
    desired_len_result = 20
    result = diary.reading_chunk(20, 1)
    num_words = len(result.split())
    assert num_words == desired_len_result 

def test_6_words_2_wpm_2_mins_called_twice():
    words = "one two three four five six"
    diary = DiaryEntry('foo', words)
    desired_len_result_first_call = 4
    first_call_result = diary.reading_chunk(2, 2)
    first_call_num_words = len(first_call_result.split())
    assert first_call_num_words == desired_len_result_first_call
    assert first_call_result == "one two three four"

    desired_len_result_second_call = 2
    second_call_result = diary.reading_chunk(2, 2)
    second_call_num_words = len(second_call_result.split())
    assert second_call_result == "five six"
    assert second_call_num_words == desired_len_result_second_call


def test_6_words_2_wpm_2_mins_called_three_times():
    words = "one two three four five six"
    diary = DiaryEntry('foo', words)
    desired_len_result_first_call = 4
    first_call_result = diary.reading_chunk(2, 2)
    first_call_num_words = len(first_call_result.split())
    assert first_call_num_words == desired_len_result_first_call
    assert first_call_result == "one two three four"

    desired_len_result_second_call = 2
    second_call_result = diary.reading_chunk(2, 2)
    second_call_num_words = len(second_call_result.split())
    assert second_call_result == "five six"
    assert second_call_num_words == desired_len_result_second_call

    desired_len_result_third_call = 4
    third_call_result = diary.reading_chunk(2, 2)
    third_call_num_words = len(third_call_result.split())
    assert third_call_result == "one two three four"
    assert third_call_num_words == desired_len_result_third_call

def test_6_words_6_wpm_one_min_whole_context_each_time():
    words = "one two three four five six"
    diary = DiaryEntry('foo', words)
    desired_len_result_first_call = 6
    first_call_result = diary.reading_chunk(6, 1)
    first_call_num_words = len(first_call_result.split())
    assert first_call_num_words == desired_len_result_first_call
    assert first_call_result == "one two three four five six"

    desired_len_result_second_call = 6
    second_call_result = diary.reading_chunk(6, 1)
    second_call_num_words = len(first_call_result.split())
    assert second_call_num_words == desired_len_result_second_call
    assert second_call_result == "one two three four five six"
