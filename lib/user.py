from typing import Type
import re

class User:
    def __init__(self):
        self.diary = []
        self.todo_list = []

    def add_diary_entry(self, entry):
        self.diary.append(entry)
    
    def read_diary(self):
        return self.diary

    def find_best_diary_entries_for_reading_time(self, wpm, minutes):
        if type(wpm) != int or type(minutes) != int: raise TypeError("Error: wpm and minute must be int")
        if wpm < 1 or minutes < 1: raise Exception("Error: wpm and minute must be greater than zero")
        return [i for i in self.diary if i.reading_time(wpm) <= minutes]
        
    def add_todo_task(self, todo):
        self.todo_list.append(todo)

    def todo_complete(self):
        return [i for i in self.todo_list if i.b_is_complete==True]

    def todo_incomplete(self):
        return [i for i in self.todo_list if i.b_is_complete==False]
    
    def get_contacts(self):
        #go through all diary entries
        #obtain all mobile number out of them
        num = []
        for i in self.diary:
            nums_in_entry = re.findall(r"\b07[0-9]\d{8}\b",i.contents)
            for j in nums_in_entry:
                mobile_number = "".join(j)
                num.append(mobile_number)
        return list(dict.fromkeys(num))