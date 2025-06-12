from lib.u_todo import *
import pytest

"""
Given non-string task of type int
raise type error
"""
def test_given_non_string_task_raise_error():
    with pytest.raises(TypeError) as err:
        UTodo(1233)
    error_message = str(err.value)
    assert error_message == "Error: non-string tasks are not allowed"
    
"""
Given empty string for task
return exception 
"""
def test_given_empty_string_task_raise_exception():
    with pytest.raises(Exception) as err:
        UTodo("")
    error_message = str(err.value)
    assert error_message == "Error: task cannot be empty"
    
"""
Given valid string task, its complete property should be false
check mark_complete
return false
"""
def test_given_valid_task_its_complete_property_should_be_false():
    obj_todo = UTodo("Go indoor bouldering")
    assert obj_todo.b_is_complete == False