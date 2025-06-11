# File: lib/todo.py
class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        if type(task) != str: raise TypeError("Error: non-string tasks are not allowed")
        if task == "": raise Exception("Error: task cannot be empty")
        self.task = task
        self.b_is_complete = False

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        self.b_is_complete = True