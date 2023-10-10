

def creatdeck():
    Deck = []

    facevalues = ["A","J","Q","K"]
    for i in range(4):
        for card in range(2,11):
            Deck.append(card)

        for card in facevalues:
            Deck.append(facevalues)
    return Deck
cardDeck = creatdeck()
print(cardDeck)
