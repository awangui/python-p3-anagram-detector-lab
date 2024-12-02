class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def is_anagram(self, word):
        return sorted(self.word) == sorted(word)

    def match(self, words):
        return [word for word in words if self.is_anagram(word.lower())]
