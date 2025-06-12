# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can record my experiences
I want to keep a regular diary

As a user
So that I can reflect on my experiences
I want to read my past diary entries

As a user
So that I can reflect on my experiences in my busy day
I want to select diary entries to read based on how much time I have and my reading speed

As a user
So that I can keep track of my tasks
I want to keep a todo list along with my diary

As a user
So that I can keep track of my contacts
I want to see a list of all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

```python
class User:
    # User-facing properties:
    #   todo_list: list of instances of todo
    #   diary: list of all instance of diary entry
    #   contacts: list of all mobile number

    def __init__(self):
        pass # No code here yet

    def add_diary_entry(self, entry):
        # Parameters:
        #   entry = diary entry object
        # Side effects:
        #   add diary entry to diary list

    def read_diary(self):
        #return a list of all diary entries objects:
        pass # No code here yet

    def find_best_diary_entries_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm: int
        #   mintue: int
        # Returns:
        #   A list of all the entries the user can read within the given time
        pass # No code here yet
    
     def add_todo_task(self, todo):
        # Parameters:
        #   todo: todo
        # side effect:
        #   add todo into todo_list
        pass # No code here yet

     def todo_complete(self):
        # return:
        #   list of all completed todo tasks
        pass # No code here yet
    
     def todo_incomplete(self):
        # return:
        #   list of all incompleted task
        pass # No code here yet
    

    def get_contacts(self):
        #return:
        #   a list of all contacts obtained from diary entries
        pass
    
class Todo:
    # User-facing properties:
    #   task: string
    #   complete: boolean

    def __init__(self, task):
        # Parameters:
        #   task: string
        # Side-effects:
        #   Sets  properties of task and complete
        pass # No code here yet

    def mark_complete(self):
        # Side effect:
        #   Sets complete property to True
        pass # No code here yet


class DiaryEntry:
    # User-facing properties:
    #   title: string
    #   content: string

    def __init__(self, title, content):
        # Parameters:
        #   title: string
        #   content: string
        # Side-effects:
        #   Sets the title and content properties
        pass # No code here yet

    def count_words(self):
        # Returns:
        #   A integer that represents the number of words content contains.
        pass # No code here yet
    
    def reading_time(self,wpm);
        # Parameters:
        #   wpm: how many words the user can read per minute
        # return:
        #   how long it will take to read the content of the diary entry with the given wpm 
        pass


```

## 3. Create Examples as Integration Tests

```python
# EXAMPLE

"""
Add a single diary entry into diary
output list of single diary entry
"""
obj_user = User()
obj_diary_entry = DiaryEntry("thursday", "I will be working and resting")
obj_user.add_diary_entry(obj_diary_entry)
assert user_diary.read_diary() == [obj_diary_entry]

"""
Add a multiple diary entries into diary
output list of diary entries
"""
obj_user = User()
obj_diary_entry_1 = DiaryEntry("thursday", "I will be working and resting")
obj_diary_entry_2 = DiaryEntry("fridday", "Work and rest")
obj_diary_entry_3 = DiaryEntry("Saturday", "Climbing and work")
obj_user.add_diary_entry(obj_diary_entry_1)
obj_user.add_diary_entry(obj_diary_entry_2)
obj_user.add_diary_entry(obj_diary_entry_3)
assert user_diary.read_diary() == [obj_diary_entry_1, obj_diary_entry_2, obj_diary_entry_3]

"""
Given word per minute, multiple diary entries and minutes. 
return a list of entries which the user can read fully
"""
obj_user = User()
obj_diary_entry_1 = DiaryEntry("thursday", "I will be working and resting")
obj_diary_entry_2 = DiaryEntry("fridday", "Work and rest")
obj_diary_entry_3 = DiaryEntry("Saturday", "Climbing and work")
obj_user.add_diary_entry(obj_diary_entry_1)
obj_user.add_diary_entry(obj_diary_entry_2)
obj_user.add_diary_entry(obj_diary_entry_3)
assert user_diary.find_best_diary_entries_for_reading_time(3, 1) == [obj_diary_entry_2, obj_diary_entry_3]

"""
Given single task to be added
get incomplete tasks
return the single task
"""
obj_user = User()
obj_todo = Todo("watch a film")
obj_user.add_todo_task(obj_todo)
assert obj_user.todo_incomplete() = [obj_todo]

"""
Given single task to be added and complete it
get complete tasks
return the single task
"""
obj_user = User()
obj_todo = Todo("watch a film")
obj_todo.mark_complete()
obj_user.add_todo_task(obj_todo)
assert obj_user.todo_complete() = [obj_todo]

"""
Given four task to be added
complete two task 
return complete taks list with two task
"""
obj_user = User()
obj_todo_1 = Todo("watch a film")
obj_todo_2 = Todo("go walk")
obj_todo_3 = Todo("stretch well")
obj_todo_4 = Todo("drink water")
obj_todo_4.mark_complete()
obj_todo_3.mark_complete()
obj_user.add_todo_task(obj_todo_1)
obj_user.add_todo_task(obj_todo_2)
obj_user.add_todo_task(obj_todo_3)
obj_user.add_todo_task(obj_todo_4)
assert obj_user.todo_complete() = [obj_todo_3, obj_todo_4]

"""
Given four task to be added
complete two task 
return incomplete taks list with two task
"""
obj_user = User()
obj_todo_1 = Todo("watch a film")
obj_todo_2 = Todo("go walk")
obj_todo_3 = Todo("stretch well")
obj_todo_4 = Todo("drink water")
obj_todo_4.mark_complete()
obj_todo_3.mark_complete()
obj_user.add_todo_task(obj_todo_1)
obj_user.add_todo_task(obj_todo_2)
obj_user.add_todo_task(obj_todo_3)
obj_user.add_todo_task(obj_todo_4)
assert obj_user.todo_complete() = [obj_todo_1, obj_todo_2]


"""
Given diary entries
get mobile numbers from entries 
return list of contact numbers
"""
obj_user = User()
obj_diary_entry_1 = DiaryEntry("thursday", "I will be working and resting. 07000000001")
obj_diary_entry_2 = DiaryEntry("fridday", "Work and rest. 07000000002")
obj_diary_entry_3 = DiaryEntry("Saturday", "Climbing and work. 07000000003")
obj_user.add_diary_entry(obj_diary_entry_1)
obj_user.add_diary_entry(obj_diary_entry_2)
obj_user.add_diary_entry(obj_diary_entry_3)
assert user_diary.get_contacts() == ["07000000001", "07000000002", "07000000003"]


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE


"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
