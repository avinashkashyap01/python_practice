
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
        facecardsdict = {"A": 11, "J": 10, "Q": 10, "K": 10,
                         "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
                         "7": 7, "8": 8, "9": 9, "10": 10}
        aceCounter = 0
        for card in self.hand:
            self.score += facecardsdict[card]
            if card == "A":
                 aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                 self.score -=10
                 aceCounter -=1
        return self.score

    def hit (self,card):
        self.hand.append(card)
        self.score = self.setscore()

    def play(self,newHand):
        self.hand = newHand
        self.score = self.setscore()

    def pay (self,amount):
        self.money -= amount

    def win (self,amount):
        self.money += amount

player1 = Player(["3","7","5"])
print(player1)
player1.hit("A")
player1.hit("A")
print(player1)
player1.pay(20)
print(player1.money)
player1.win(40)
print(player1.money)
player1.play(["A","K"])
print(player1)
print(player1.money)
