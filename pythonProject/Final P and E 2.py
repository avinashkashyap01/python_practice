
from random import shuffle
def creatdeck():
    Deck = []

    facevalues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(card)

        for card in facevalues:
            Deck.append(facevalues)
    shuffle(Deck)
    return Deck
cardDeck = creatdeck()
print(cardDeck)



class Player:
    def __init__(self,hand =[],money = 100):
        self.hand = hand
        self.score = self.setscore()
        print(self.score)
        self.money = money

    def __str__(self):
        currenthand = ""

        for card in self.hand:
            currenthand += str(card) + " "

        finalstatus = currenthand + "score: " +str(self.score)
        return finalstatus
    def setscore(self):
        self.score = 0
        print(self.score)
        facecardsdict = {"A":11,"J":10,"Q":10,"K":10,
                         "2":2,"3":3,"4":4,"5":5,"6":6,
                         "7":7,"8":8,"9":9,"10":10}
        aceCounter = 0
        for card in self.hand:
            self.score += facecardsdict[card]
            if card == "A":
                 aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                 self.score -=10
                 aceCounter -=1
        return self.score
player1 = Player(["3","7","5"])
print(player1)
