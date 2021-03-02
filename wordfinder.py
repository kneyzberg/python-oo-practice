from random import choice


class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, path):
        self.path = path
        self.word_list = self.create_word_list()
        print(f"{len(self.word_list)} words read")

    def create_word_list(self):
        word_list = []
        try: 
            with open(self.path) as file:
                for line in file:
                    if line.endswith("\n"):
                        word_list.append(line[:-1])
                    else: 
                        word_list.append(line)
            return word_list
        except OSError:
            print("Invalid file path")
    
    def random(self):
        return choice(self.word_list)

class SpecialWordFinder(WordFinder):
    def __init__(self, path):
        super().__init__(path)
    
    def create_word_list(self):
        word_list = super().create_word_list()
        return [word for word in word_list if not word.startswith("#") and not word == ""]


