from lib.todo import ToDo
import pytest 

def test_add_method():
    todo = ToDo()
    desired_result = "Clean up added to to-do list."
    result = todo.add("Clean up")
    assert desired_result == result

def test_view_method():
    todo = ToDo()
    todo.add("Clean up")
    todo.add("Watch TV")
    desired_result = ["Clean up", "Watch TV"]
    result = todo.view()
    assert desired_result == result

def test_view_method_exception_thrown():
    todo = ToDo()
    desired_result = "Nothing to do!"

    with pytest.raises(Exception) as e:
        todo.view()
    error_msg = str(e.value)
    assert desired_result == error_msg

def test_mark_complete_method():
    todo = ToDo()
    todo.add("Clean up")
    todo.add("Watch TV")
    desired_confirmation = "Clean up has been marked as complete!"
    confirmation_msg = todo.mark_complete("Clean up")
    assert desired_confirmation == confirmation_msg
    
    desired_view = ["Watch TV"]
    view = todo.view()
    assert desired_view == view

def test_mark_complete_method_exception_thrown():
    todo = ToDo()
    desired_result = "invalid, could not be found in to-do list."
    with pytest.raises(Exception) as e:
        todo.mark_complete("invalid")
    error_msg = str(e.value)
    assert desired_result == error_msg

