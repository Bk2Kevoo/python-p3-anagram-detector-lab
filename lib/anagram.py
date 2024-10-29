class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        sorted_given_word = "".join(sorted(self.word))
        
        return [
            word for word in word_list if sorted_given_word == "".join(sorted(word))
        ]

hello = Anagram("HELLO")
hello.match(["ohlel", "cat", "test"])
