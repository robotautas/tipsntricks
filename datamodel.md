### Specialūs metodai

Kiekviena mūsų sukurta klasė turi priėjimą prie specialių (dar vadinamų _dunder_ - double underscore) metodų. Kai kuriuos mes naudojame dažnai, pvz. \_\_init\_\_ arba \_\_repr\_\_, tačiau yra daugybė kitų, dalį jų čia apžvelgsime.

```python
class Card:
    def __init__(self, suite, rank):
        self.suite = suite
        self.rank = rank

    def __repr__(self):
        return f"Card('{self.suite}', '{self.rank}')"


c1 = Card('♦', 'Q')
print(c1)

# Card('♦', 'Q')
```

Turime paprastą kortos modelį, iš kurio galime sukurti kortos objektą, parametruose nurodydami rūšį ir rangą. \_\_repr\_\_ metodas atspausdina _developer friendly_ objekto reprezentaciją. Sukurkime _property_ metodą points, iš kuris nurodys, kiek taškų turi korta.

```python
    @property
    def points(self):
        if self.rank.isdigit():
            return int(self.rank)
        else:
            mapping = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
            return mapping[self.rank]

    # ...

c1 = Card('♦', 'Q')
print(c1.points)

# 12
```

sukurkime galimybę su kortos kortos objektais naudoti sudėties operatorių:

```python
    def __add__(self, other):
        return self.points + other.points

c1 = Card('♦', 'Q')
c2 = Card('♦', '10')
c3 = Card('♦', '3')
print(c2 + c1 + c3)

# 22
```

bet:

```python
print(c2 + c1 + c3)

# TypeError: unsupported operand type(s) for +: 'int' and 'Card'
```

Taip yra todėl, kad python pirmiausiai atlieka c1 + c2 iš to gauna integer reikšmę. Tuomet integer reikšmę bando sudėti su c3, tačiau \_\_add\_\_ metodas nepalaiko objekto sudėties su integer'iu. Reikalingas kitas metodas:

```python
    def __radd__(self, other):
        return self.points + other


c1 = Card('♦', 'Q')
c2 = Card('♦', '10')
c3 = Card('♦', '3')
print(c2 + c1 + c3)
```

dabar galime sudėti kiek norime objektų. Taip pat prie kortos pridėti tiesiog skaičių, ar naudoti su kortų rinkiniu sum metodą. Įgyvendinkime atimtį:

```python
    def __sub__(self, other):
        return self.points - other.points

    def __rsub__(self, other):
        return other - self.points


c1 = Card('♦', 'Q')
c2 = Card('♦', '10')
c3 = Card('♦', '3')
print(c1 - c2 - c3)

# -1
```

daugyba ir dalyba kortų žaidime nereikalingos, bet galime įgyvendinti analogiškai:

```python
    def __mul__(self, other):
        return self.points * other.points

    def __rmul__(self, other):
        return other * self.points

    def __truediv__(self, other):
        return self.points / other.points

    def __rtruediv__(self, other):
        return other / self.points


c1 = Card('♦', 'Q')
c2 = Card('♦', '10')
c3 = Card('♦', '3')
print(c1 * c2 * c3)
print(c1 / c2 / c3)

# 360
# 0.39999999999999997
```

Taip pat nesunkiai įgyvendinamas lyginamųjų operatorių panaudojimas, kad galėtumėm objektus lyginti tarpusavy :

| `__lt__` | `obj < ...`  | les than      |
| -------- | ------------ | ------------- |
| `__le__` | `obj <= ...` | less equal    |
| `__eq__` | `obj == ...` | equal         |
| `__ne__` | `obj != ...` | not equal     |
| `__gt__` | `obj > ...`  | greater than  |
| `__ge__` | `obj >= ...` | greater equal |

pvz:

```python
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
```

Susikurkime klasę kortų rinkiniui:

```python
class Deck:
    def __init__(self, *cards):
        self.cards = cards

    def __repr__(self):
        return f'Deck{self.cards}'


d1 = Deck(c1, c2, c3, c4)
print(d1)
class Deck:
    def __init__(self, *cards):
        self.cards = cards

    def __repr__(self):
        return f'Deck{self.cards}'


d1 = Deck(c1, c2, c3, c4)
print(d1)

# Deck(Card('♦', 'Q'), Card('♦', '10'), Card('♦', '3'), Card('♥', '3'))
```

padarykime šios klasės objektus iteruojamais:

```python
    def __iter__(self):
        return iter(self.cards)


d1 = Deck(c1, c2, c3, c4)

for card in d1:
    print(card)

# Card('♦', 'Q')
# Card('♦', '10')
# Card('♦', '3')
# Card('♥', '3')
```

suteikime objektams kitas sąrašo savybes:

```python
    def __getitem__(self, position):
        return self.cards[position]

    def __setitem__(self, position, value):
        self.cards[position] = value

    def __delitem__(self, position):
        del self.cards[position]

    def __contains__(self, value):
        return value in self.cards


d1 = Deck(c1, c2, c3, c4)

print(d1[2])

d1[1] = 'bananas'
print(d1)

del d1[1]
print(d1)

print(Card('♦', 'Q') in d1)

# Card('♦', '3')
# Deck[Card('♦', 'Q'), 'bananas', Card('♦', '3'), Card('♥', '3')]
# Deck[Card('♦', 'Q'), Card('♦', '3'), Card('♥', '3')]
# True
```

įdėkime len metodą:

```python
    def __len__(self):
        return len(self.cards)


print(len(d1))
# 3
```

Daugiau pavyzdžių ir informacijos šia tema:
https://www.oreilly.com/library/view/fluent-python-2nd/9781492056348/ch01.html
