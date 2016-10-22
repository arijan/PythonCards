# cards demo

# lets have a list of ranks and suits
ranks = list(map(str, range(2,11))) + list('JQKA')
suits = list('SDCH')
suitSyms = dict(zip(suits, list('♠♦♣♥')))

# make local variables out of them
for v in ranks:
    locals()[v] = v
for v in suits:
    locals()[v] = v

# Singleton metaclass
class SingletonOfEachKind(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        key = args + tuple(kwargs)
        if key not in cls._instances:
            cls._instances[key] = super(SingletonOfEachKind, cls).__call__(*args, **kwargs)
        return cls._instances[key]
    
class Card(metaclass=SingletonOfEachKind):
    """ Card(rank, suite) is a single card """
    def __init__(self, r, s):
        if r in ranks and s in suits:
            self.__rank = r
            self.__suit = s
        else:
            raise LookupError('Rank {} or suit {} does not exsist.'.format(r, s))

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
        self.cards = []
        
    def FullDeck(self):
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
            raise LookupError('Card {} not in fromDeck {}.'.format(c, self.cards))

    def append(self, c):
        if c in self:
            raise LookupError('Card {} already in toDeck {}.'.format(c, self.cards))
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

def DealHand(deck, hand):
    for c in range(0, 5):
        TakeCard(deck.topCard(), deck, hand)
        
d=Deck().FullDeck()
h=Deck()
TakeCard(Card(A, S), d, h)
print(Card(A, S) in d)
print(Card(A, S) in h)
h2=Deck()
DealHand(d, h2)
print(h2)
h3=Deck()
d.shuffle()
DealHand(d, h3)
print(h3)
