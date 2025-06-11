# File: lib/todo_list.py
class TodoList:
    def __init__(self):
        self._todo = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self._todo.append(todo)        

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        return [i for i in self._todo if i.b_is_complete==False]

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        return [i for i in self._todo if i.b_is_complete==True]

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for i in self._todo: i.mark_complete()
