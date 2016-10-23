# cards demo

# lets have a list of ranks and suits
ranks = list(map(str, range(2, 11))) + list('JQKA')
suits = list('SDCH')
suitSyms = dict(zip(suits, list('♠♦♣♥')))

# make local variables out of them
for v in ranks:
    locals()[v] = v
for v in suits:
    locals()[v] = v


class ObjectSameForGivenParameters(type):
    """ Object with same setup parameters will be same object not a new one."""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        key = args + tuple(kwargs)
        if key not in cls._instances:
            cls._instances[key] = super(ObjectSameForGivenParameters, cls).__call__(*args, **kwargs)
        return cls._instances[key]
    

class Card(metaclass=ObjectSameForGivenParameters):
    """ Card(rank, suite) is a single card """
    def __init__(self, r, s):
        if r in ranks and s in suits:
            self.__rank = r
            self.__suit = s
        else:
            raise LookupError('Rank {} or suit {} does not exist.'.format(r, s))

    @property
    def rank(self):
        return self.__rank
    
    @property
    def suit(self):
        return self.__suit

    def __repr__(self):
        return "Card({}, {})".format(self.rank, self.suit)

    def __str__(self):
        return self.rank + suitSyms[self.suit]
    
from collections import Sequence
import random


class Deck(Sequence):
    """ Deck of cards """
    def __init__(self):
        self.emptyDeck()

    def emptyDeck(self):
        self.cards = []
        return self
        
    def fullDeck(self):
        self.cards = [Card(r, s) for s in suits for r in ranks]
        return self

    def __contains__(self, key):
        return key in self.cards

    def __len__(self):
        return len(self.cards)

    def __getitem__(self, i):
        return self.cards[i]
    
    def index(self, *args):
        return self.cards.index(*args)
    
    def remove(self, c):
        if c in self:
            self.cards.remove(c)
        else:
            raise LookupError('Card {} not in remove deck {}.'.format(c, self.cards))

    def append(self, c):
        if c in self:
            raise LookupError('Card {} already in append deck {}.'.format(c, self.cards))
        else:
            self.cards.append(c)

    def __repr__(self):
        return str(self.cards)

    def __str__(self):
        return " ".join(map(str, self.cards))
    
    def shuffle(self):
        random.shuffle(self.cards)

    def topCard(self):
        return self.cards[0]
        

def TakeCard(card, fromDeck, toDeck):
    fromDeck.remove(card)
    toDeck.append(card)


def TopCard(deck):
    return deck.topCard()


def DealHand(deck, hand):
    for c in range(0, 5):
        TakeCard(TopCard(deck), deck, hand)


def Shuffle(deck):
    deck.shuffle()

# simple tests
deck1 = Deck().fullDeck()
hand1 = Deck().emptyDeck()
TakeCard(Card(A, S), deck1, hand1)
print(Card(A, S) in deck1)
print(Card(A, S) in hand1)

h2 = Deck()
DealHand(deck1, h2)
print(h2)

h3 = Deck().emptyDeck()
Shuffle(deck1)
DealHand(deck1, h3)
print(h3)
