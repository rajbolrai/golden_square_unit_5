from lib.todo_list import *

""" 
When no todo object has been added
getting incomplete list
returns empty list
"""
def test_given_no_todo_output_empty_incomplete_list():
    obj_todo_list = TodoList()
    assert obj_todo_list.incomplete() == []

""" 
When no todo object has been added
getting complete list
returns empty list
"""
def test_given_no_todo_output_empty_complete_list():
    obj_todo_list = TodoList()
    assert obj_todo_list.complete() == []
