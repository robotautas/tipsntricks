suites = '♦ ♥ ♣ ♠'


class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __repr__(self):
        return f"Card('{self.suite}', '{self.rank}')"

    @property
    def points(self):
        if self.rank.isdigit():
            return int(self.rank)
        else:
            mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            return mapping[self.rank]

    def __add__(self, other):
        return self.points + other.points

    def __radd__(self, other):
        return self.points + other

    def __sub__(self, other):
        return self.points - other.points

    def __rsub__(self, other):
        return other - self.points

    def __mul__(self, other):
        return self.points * other.points

    def __rmul__(self, other):
        return other * self.points

    def __truediv__(self, other):
        return self.points / other.points

    def __rtruediv__(self, other):
        return other / self.points

    def __lt__(self, other):
        return self.points < other.points

    def __le__(self, other):
        return self.points <= other.points

    def __eq__(self, other):
        return self.points == other.points

    def __gt__(self, other):
        return self.points > other.points

    def __ge__(self, other):
        return self.points >= other.points


c1 = Card('♦', 'Q')
c2 = Card('♦', '10')
c3 = Card('♦', '3')
c4 = Card('♥', '3')


class Deck:
    def __init__(self, *cards):
        self.cards = list(cards)

    def __repr__(self):
        return f'Deck{self.cards}'

    def __iter__(self):
        return iter(self.cards)

    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, value):
        self.cards[position] = value

    def __delitem__(self, position):
        del self.cards[position]

    def __contains__(self, value):
        return value in self.cards

    def __len__(self):
        return len(self.cards)


d1 = Deck(c1, c2, c3, c4)
