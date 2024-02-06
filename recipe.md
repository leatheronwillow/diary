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

nouns = [diary, entries, todo list, tasks, contacts, mobile phone numbers]
verbs = [record, read, select, keep track, ]

```
  ┌──────────────────────────────────────────────┐
  │                                              │
  │   Diary                                      │
  │                                              │
  │  - entries                                   │
  │  - contacts                                  │
  │  - add_entry(Entry)                          │
  │  - read_entry(Entry)                         │        ┌────────────────────────────┐
  │    => "Title: Contents"                      │        │  ToDoList(entry)           │
  │  - select_entry(wpm, mins)                   │        │                            │
  │    => Entry                                  │        │ - tasks                    │
  │  - view_contacts()                           │        │ - view_list()              │
  │    => [{contact1.name: contact1.number},...] │        │   => [entry1, entry2...]   │
  │                                              │        └────┬───────────────────────┘
  └──────────────────────────────────────┬───────┘             │
                                         │                     │
                                         │                     │
                           owns a list of│                     │owns a list of
                                         │                     │
                                         │                     │
                                         │                     │
                                     ┌───▼─────────────────────▼────┐
                                     │                              │
                                     │   Entry(title, contents)     │
                                     │                              │
                                     │ - title                      │
                                     │ - contents                   │
                                     │ - add(title, contents)       │
                                     │                              │
                                     └──────────────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Diary():
    # User facing properties:
    #   entries: a list of instances of entries
    #   contacts: a list of strings containing phone numbers

    def __init__(self):
        pass

    def add_entry(self, title, contents):
        # Parameters:
        #     title: string
        #     contents: a string

        # Side-effects:
        #     Adds an instance of Entry to the list of entries
        #     If it contains a phone number, also add the entry to a separate list of contacts
        pass
    

    def read_entry(self, title):
        # Parameters:
        #     title: a string conatining the title of an entry
        # Returns:
        #     the entry in the given format "Title: Contents"
        pass

    def select_entry(self, wpm, mins):
        # Parameters:
        #     wpm: integer for reading speed
        #     mins: integer  for time the person has to read
        # Returns:
        #     an instance of entry with the largest entry that the reader can read in the given time
        pass

    def view_contacts(self):
        # Returns:
            # A list of contacts with phone numbers.
        pass

    def _is_phone_number(self, entry):
        # Parameters:
        #     entry: instance of Entry
        # Returns:
        #     boolean which is true if the entry contains a phone number
        pass 
        

class ToDoList():
    # User-facing properties:
    #     tasks: list of instances of entry

    def __init__(self):
        pass

    def add_task(self, task, complete=False):
        # Parameters:
        #     task: a string containing the task
        #     complete: a boolean value to keep track of whether the task has been completed
        #     which defaults to False
        # Side-effects:
        #     creates an entry and adds it to the tasks list.
        pass
    
    def view_tasks(self):
        # Returns:
        #     A list of incomplete tasks
        pass

class Entry():
    # User-facing properties:
    #   title: string
    #   contents: string

    def __init__(self, title, contents):
        # Parameters:
        #     title: string
        #     contents: string

        # Side-effects: 
        #     Initiates class with given title and contents
        pass

    def replace_contents(self, contents):
        # Parameters:
        #     contents: string or boolean
        # Side-effects:
        #     replaces contents of given class
        pass

    def replace_title(self, title):
        # Parameters:
        #     title: string
        # Side-effects:
        #     replaces the title of the Entry with given title.
        pass

    def count_words(self):
        # Returns:
        #     An int word count for the entry
        pass

    def get_contents(self):
        # Returns:
        #     A string or boolean contianing the contents property
        pass
    
    def format(self):
        # Returns:
        #     A formatted diary entry, for example:
        #     "My Title: These are the contents"
        pass


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]

"""
Given a diary
When we add a diary entry, it is reflected back in the entries list
"""
diary = Diary()
diary.add_entry("Title", "Contents")
diary.entries[0].title => "Title"
diary.entries[0].contents => "Contents"
isinstance(diary.entries[0], Entry) => True

"""
Given an entry title,
find and return the entry in the given format
"""

diary = Diary()
diary.add_entry("Title", "Contents")
diary.read_entry("Title") => "Title: Contents"



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


# Diary
"""
initialise diary
"""
diary = Diary()
isinstance(diary, Diary) => True

# Entry

"""
Given an entry with a title and contents
We see the title reflected back in the title property
We see the contents reflected back in the contents property
"""
entry = Entry("title", "contents")
entry.title => "title"
entry.contents => "contents"

"""

"""

# ToDoList
"""

"""
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._