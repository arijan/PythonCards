# cards demo

# lets have a list of ranks and suits
ranks = list(map(str, range(2,11))) + list('JQKA')
suits = list('SDCH')

# make local variables out of them
for v in ranks:
    locals()[v] = v
for v in suits:
    locals()[v] = v
    
class Card:
    """ Card(rank, suite) is a single card """
    def __init__(self, r, s):
        if r in ranks and s in suits:
            self.rank = r
            self.suit = s
        else:
            raise LookupError('Rank {} or suit {} does not exsist.'.format(r, s))

    def __repr__(self):
        return "Card({}, {})".format(self.rank, self.suit)

class Deck:
    """ Deck of cards """
    def __init__(self):
        self.cards = []
        
    def FullDeck(self):
        self.cards = [Card(r, s) for s in suits for r in ranks]
        return self

    def findCard(self, c):
        for x in self.cards:
            if x.rank == c.rank and x.suit == c.suit:
                return x
        else:
            return False

    def __contains__(self, c):
        if self.findCard(c):
            return True
        else:
            return False
        
    def remove(self, c):
        x = self.findCard(c)
        if x:
            self.cards.remove(x)
        else:
            raise LookupError('Card {} not in fromDeck {}.'.format(c, self.cards))

    def append(self, c):
        x = self.findCard(c)
        if x:
            raise LookupError('Card {} already in toDeck {}.'.format(c, self.cards))
        else:
            self.cards.append(c)

    def __repr__(self):
        return str(self.cards)
        
def TakeCard(card, fromDeck, toDeck):
    fromDeck.remove(card)
    toDeck.append(card)


d=Deck().FullDeck()
h=Deck()
TakeCard(Card(A, S), d, h)
print(Card(A, S) in d)
print(Card(A, S) in h)
