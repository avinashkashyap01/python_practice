
# Static and Instance Methods

class wordset:
    def __init__(self):
        self.word = set()

    def addtext(self,text):
        text = self.cleantext(text)
        for word in text.split():
            self.word.add(word)

    def cleantext(self,text):
        text = text.replace('!','').replace('.','').replace(',','').replace('\'','')
        return text.lower()

wordset = wordset()

wordset.addtext('Hi, I\'m Avinash! Here is a sentence I want to add!')
wordset.addtext(' Here is another sentence I want to add!')

print(wordset.word)


# Decoraters
class wordset:
    replacepuncs = ['!','.',',','\'']
    def __init__(self):
        self.word = set()

    def addtext(self,text):
        text = self.cleantext(text)
        for word in text.split():
            self.word.add(word)
    @staticmethod
    def cleantext(text):
        for punc in wordset.replacepuncs:
            text = text.replace(punc,'')
        return text.lower()

wordset = wordset()

wordset.addtext('Hi, I\'m Avinash! Here is a sentence I want to add!')
wordset.addtext(' Here is another sentence I want to add!')

print(wordset.word)
