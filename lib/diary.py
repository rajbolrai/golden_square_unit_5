from lib.diary_entry import * 

class Diary:
    def __init__(self):
        self._diary_entries = []
        self._curr_word_count = 0

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self._diary_entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self._diary_entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        self._curr_word_count = sum([i.count_words() for i in self._diary_entries])
        return self._curr_word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if len(self._diary_entries) == 0: raise Exception("No entries in diary. Unable to calculate reading time.")
        if wpm <= 0: raise Exception("Error: wpm cannot be less than 1")
        return math.ceil(self.count_words()/wpm)
                
    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        length = len(self._diary_entries)
        if length == 0: raise Exception("No entries in diary. Unable to find best entry.")
        
        words_to_read = wpm * minutes 
        closest_instance = None
        closest_length = 0
        for i in range(0, length):
            curr_entry =self._diary_entries[i].count_words()
            if curr_entry > closest_length and curr_entry <= words_to_read:
                closest_instance = self._diary_entries[i]
                closest_length = curr_entry

        return closest_instance if closest_instance != None else "Unable to read any entries within the given time"

