class UTodo:
    def __init__(self, task):
        if type(task) != str: raise TypeError("Error: non-string tasks are not allowed")
        if task == "": raise Exception("Error: task cannot be empty")
        self.task = task
        self.b_is_complete = False

    def mark_complete(self):
        self.b_is_complete = True