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
        self.title = title
        self.contents = contents
        pass

#     def replace_contents(self, contents):
#         # Parameters:
#         #     contents: string or boolean
#         # Side-effects:
#         #     replaces contents of given class
#         pass

#     def replace_title(self, title):
#         # Parameters:
#         #     title: string
#         # Side-effects:
#         #     replaces the title of the Entry with given title.
#         pass

#     def count_words(self):
#         # Returns:
#         #     An int word count for the entry
#         pass

#     def get_contents(self):
#         # Returns:
#         #     A string or boolean contianing the contents property
#         pass
    
#     def format(self):
#         # Returns:
#         #     A formatted diary entry, for example:
#         #     "My Title: These are the contents"
#         pass