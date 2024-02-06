from lib.entry import Entry

class Diary():

    def __init__(self):
        self.entries = []
        return None

    def add_entry(self, title, contents):
        # Parameters:
        #     title: string
        #     contents: a string

        # Side-effects:
        #     Adds an instance of Entry to the list of entries
        #     If it contains a phone number, also add the entry to a separate list of contacts
        entry = Entry(title, contents)
        self.entries.append(entry)
        return None
    


    def read_entry(self, title_):
        # Parameters:
        #     title: a string conatining the title of an entry
        # Returns:
        #     the entry in the given format "Title: Contents"
        for entry in self.entries:
            if entry.title == title_:
                return entry.format()

    # def select_entry(self, wpm, mins):
    #     # Parameters:
    #     #     wpm: integer for reading speed
    #     #     mins: integer  for time the person has to read
    #     # Returns:
    #     #     an instance of entry with the largest entry that the reader can read in the given time
    #     pass

    # def view_contacts(self):
    #     # Returns:
    #         # A list of contacts with phone numbers.
    #     pass

    # def _is_phone_number(self, entry):
    #     # Parameters:
    #     #     entry: instance of Entry
    #     # Returns:
    #     #     boolean which is true if the entry contains a phone number
    #     pass 