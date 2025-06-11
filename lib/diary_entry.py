# File: lib/diary_entry.py
from os import read
import re
import math

class DiaryEntry:
    # Public Properties:
    #   title: a string
    #   contents: a string

    def __init__(self, title, contents): # title, contents are strings
        # Side-effects:
        #   Sets the title and contents properties
        if type(title) != str or type(contents) != str : raise TypeError("Invalid type, title and content must be string") 
        if title == "" or contents == "" : raise TypeError("Title and content cannot be empty") 

        self._title = title
        self._contents = contents
        self._content_words = re.findall(r"\b[a-zA-Z]+(?:'[a-zA-Z]+)?(?:-[a-zA-Z'.?!]+)*(?:[?!.]+)?(?!\w)", self._contents)
        self._read_so_far = 0
        
    # Add this method for developer-friendly representation (used by lists)
    def __repr__(self):
        return self._title
    
    def count_words(self):
        # Returns:
        #   An integer representing the number of words in the contents
        return len(self._content_words)
        

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   for the contents at the given wpm.
        if wpm < 1: raise Exception("Error: wpm cannot be lower than 1")
        reading_time = len(self._content_words)/wpm
        return math.ceil(reading_time)
        

    def reading_chunk(self, wpm, minutes):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   A string representing a chunk of the contents that the user could
        #   read in the given number of minutes.
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that it should restart from the beginning.
        
        if wpm < 1 or minutes < 1: raise Exception("Error: wpm and minute cannot be lower than 1")
        words_to_read = wpm * minutes
        if self._read_so_far >= self.count_words(): self._read_so_far = 0
        ending_index = self._read_so_far + words_to_read
        chunk = " ".join(self._content_words[self._read_so_far:ending_index])
        self._read_so_far = ending_index
    
        return chunk