class VowelRemover:
    def __init__(self, text):
        self.text = text
        self.vowels = ["a", "e", "i", "o", "u"]

    def remove_vowels(self):
        i = 0
        final = ""
        while i < len(self.text):
            if self.text[i].lower() not in self.vowels:
                final += self.text[i]
            i += 1
        return final

test_vowel = VowelRemover("aeiodfgsdgu")
test_vowel.remove_vowels()