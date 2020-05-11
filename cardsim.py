# Name: Jadyn Kennedy
# Date: 5/11/2
# Citations: Emmanuel Batista (helped me better understand what the append function does)


import random
def copywrite():
    c = "This simulator was created by Jadyn Kennedy 5/11/2020"
    print(c)

class Card:
    def __init__(card, rank, suit):
        card.rank = rank #creates instance variable for rank
        card.suit = suit #creates instance variable for suit
        
    def getRank(card):
        if card.rank == 13:
            name = "king"
        elif card.rank == 12:
            name = "queen"
        elif card.rank == 11:
            name = "jack"
        elif card.rank == 1:
            name = "ace"
        else:
            name = int(card.rank) #allows "name" to be any other integer in our set range
        return name

    def getSuit(card):
        return card.suit


class Deck:
    def __init__(card, deck):
        card.deck = deck
    
    def suffle(card):
        random.shuffle(card.deck)
        card.deck.insert(0, "joker") #assures that the "first card" on the deck is one that can be tossed (I just named mine joker because we generally discard the jokers anyway)

    def draw(card):
        del card.deck[0] #this makes sure that it's only printing one card020 and moving on (and doesn't repeat that card later), deleting "firstCard" instead of an actual card
        return card.deck[0] #returns the new value of the first card on the deck
        

def main():
    Title = "Card Suffle Simulator"
    print(Title)
    suits = ["spades", "hearts", "diamonds", "clubs"] 
    ranks = range(1, 14)  #account for ace, king, queen etc in Card class
    cards = [] #creates an empty "deck" of cards that will be adjusted later
    for a in ranks:
        for b in suits:
            cards.append(Card(a, b)) #creates the values for the cards (makes sure there is one of each)
    deck = Deck(cards) #updating the appended card value
    deck.suffle()
    cardList = range(52) #makes sure to print up to 52 cards (this is why it is important to delete the "top" card on the deck every time
    for i in cardList:
        c = deck.draw()
        print(c.getRank(), "of", c.getSuit())

    copywrite()

main()
