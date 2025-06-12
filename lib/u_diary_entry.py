import re
import math

class UDiaryEntry:
    def __init__(self, title, content):
        if type(title) != str or type(content) != str : raise TypeError("Invalid type, title and content must be string") 
        if title == "" or content == "" : raise TypeError("Title and content cannot be empty") 

        self.title = title
        self.contents = content
        self.content_words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?(?:-[a-zA-Z'.?!]+)*(?:[?!.]+)?(?!\w)", self.contents)

    def count_words(self):
        return len(self.content_words)
    
    def reading_time(self,wpm):
        if type(wpm) != int : raise TypeError("Error: wpm must be int")
        if wpm < 1: raise Exception("Error: wpm has to be 1 or higher")
        return math.ceil(self.count_words()/wpm)
