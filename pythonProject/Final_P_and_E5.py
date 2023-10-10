
from random import shuffle
def createdeck():
    Deck = []

    facevalues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(card)

        for card in facevalues:
            Deck.append(facevalues)
    shuffle(Deck)
    return Deck
cardDeck = createdeck()
print(cardDeck)



class Player:
    def __init__(self,hand =[],money = 100):
        self.hand = hand
        self.score = self.setscore()
        self.money = money
        self.bet = 0

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

    def betmoney(self,amount):
        self.money -= amount
        self.bet += amount

    def win (self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5*self.bet
            else:
              self.money += 2*self.bet

            self.bet = 0
        else:
            self.bet = 0

def printhouse(house):
    for card in range(len(house.hand)):
        if card == 0:
            print("X",end=" ")
        elif card == len(house.hand) - 1:
            print(house.hand[card])
        else:
            print(house.hand[card],end=" ")

cardDeck = createdeck()

firsthand = [cardDeck.pop(),cardDeck.pop()]
secondhand = [cardDeck.pop(),cardDeck.pop()]
player1 = Player(firsthand)
house = Player(secondhand)
print(cardDeck)
printhouse(house)
print(player1)
while(player1.score < 21):
    action = input("do you want another card? (y/n):")
    if action == "y":
        player1.hit(cardDeck.pop())
        print(player1)
        printhouse(house)
    else:
        break
print(house)
