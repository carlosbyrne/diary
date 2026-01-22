class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.__index = 0
        

    def format(self):
        # Returns:
        #   A formatted diary entry, for example:
        #   "My Title: These are the contents"
        title = self.title
        contents = self.contents
        if not isinstance(title, str) or not isinstance(contents, str):
            raise Exception("Invalid diary entry.")
        return f"{title}: {contents}"
        

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        contents = self.contents
        if not isinstance(contents, str):
            raise Exception("Invalid diary entry.")
        words = contents.split()
        return len(words)
        

    def reading_time(self, wpm: int):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        contents = self.contents
        if contents == "" or not isinstance(contents, str) or not isinstance(wpm, int):
            raise Exception("Invalid diary entry.")
        one_min_words = wpm
        words = len(contents.split())
        time = words / one_min_words
        return time
        

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        contents = self.contents
        words = contents.split()
        current_index = self.__index
        end_index = current_index + (wpm * minutes)
        if current_index == 0:
            chunk = words[current_index:end_index]
            chunk_str = " ".join(word for word in chunk)
            if end_index < len(words):
            # If we can set the current end index to be the next start index
            # then we do so, so then we dont recapture the contents we already returned with the first call
                self.__index += end_index
            else:
            # We dont want an index error -- if we can print the whole contents first time
            # then just reset the start index again
                self.__index = 0
            return chunk_str
        else:
            chunk = words[current_index:]
            chunk_str = " ".join(word for word in chunk)
            self.__index = 0
            return chunk_str
            
