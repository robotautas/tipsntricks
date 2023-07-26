# Tuples

Tuplas yra nekintama iteruojama duomenų kolekcija python'e.

```python
savaite = ('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis', 'penktadienis', 'sestadienis', 'sekmadienis')

print(savaite)
print(type(savaite))

#('pirmadienis', 'antradienis', 'treciadienis', 'ketvirtadienis', 'penktadienis', 'sestadienis', 'sekmadienis')
#<class 'tuple'>
```

tuplas koks deklaruojamas, toks ir išlieka visą laiką:

```python
savaite.append('astuntadienis')
# AttributeError: 'tuple' object has no attribute 'append'
```

```python
savaite[0] = 'kitadienis'
# 'tuple' object does not support item assignment
```

## Tuple'ų privalumai:

- Veikia greičiau už listus
- Tam tikrose situacijose užtikrina saugumą
- Galima naudoti kaip raktus žodyne

```python
coords = {
    (54.677778, 25.291667): 'Vilnius',
    (54.897222, 23.886111): 'Kaunas'
}
```

## Iteracija

Iteruoti per tuple'us galima taip pat, kaip ir per sąrašus:

```python
for diena in savaite:
    print(diena)

# pirmadienis
# antradienis
# treciadienis
# ketvirtadienis
# penktadienis
# sestadienis
# sekmadienis
```

taip pat veikia ir indeksacija bei pjūviai:

```python
print(savaite[1])
print(savaite[0:2])

# antradienis
# ('pirmadienis', 'antradienis')
```

## Tuple'ų metodai:

.count():

```python
x = (1,2,3,3,3,3)

print(x.count(2)) #1
print(x.count(3)) #4
```

.index():

```python
print(x.index(2)) #1
print(x.index(3)) #2
```

# Sets

Set'ai taip pat yra duomenų kolekcija, kurios pagrindinės savybės yra:

- neegzistuoja eiliškumas
- negali būti dublikatų

```python
vardai = {'Jurgis', 'Antanas', 'Aloyzas', 'Martynas'}

print(vardai)
print(type(vardai))

# {'Antanas', 'Aloyzas', 'Jurgis', 'Martynas'}
# <class 'set'>
```

```python
print(vardai[1])
# TypeError: 'set' object is not subscriptable
```

```python
sarasas = [1, 2, 3, 4, 4, 5, 5]
setas = set(sarasas)
print(setas)
# {1, 2, 3, 4, 5}
```

## Iteracija

```python
for num in setas:
    print(num)

# 1
# 2
# 3
# 4
# 5
```

## Panaudojimo galimybės

be dublikatų išmetimo iš rinkinio galima sutikrinti, kokie nariai aptikti dviejuose skirtinguose set'uose:

```python
miestai_1 = {'Vilnius', 'Kaunas', 'Klaipėda',}
miestai_2 = {'Kaunas', 'Klaipėda', 'Šiauliai', 'Panevėžys'}

sutampantys_miestai = miestai_1 & miestai_2
print(sutampantys_miestai)
# {'Klaipėda', 'Kaunas'}
```

Taip pat apjungti setus į vieną, eliminuojant dublikatus:

```python
apjungti_setai = miestai_1 | miestai_2
print(apjungti_setai)
# {'Klaipėda', 'Kaunas', 'Šiauliai', 'Panevėžys', 'Vilnius'}
```

## Metodai

.add()

```python
miestai = {'Vilnius', 'Kaunas', 'Klaipėda'}
miestai.add('Šiauliai')
print(miestai)
# {'Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai'}
```

.remove():

```python
miestai = {'Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai'}
miestai.remove('Šiauliai')
print(miestai)
# {'Vilnius', 'Klaipėda', 'Kaunas'}
```

.discard():

```python
# Tas pats, kaip remove, tik nemeta klaidos, jeigu bandome ištrinti neegzistuojantį narį
miestai = {'Vilnius', 'Kaunas', 'Klaipėda', 'Šiauliai'}
miestai.discard('Alytus')
miestai.discard('Kaunas')
print(miestai)
# {'Vilnius', 'Šiauliai', 'Klaipėda'}
```

.clear() - išvalo set'ą
.copy() - padaro set'o kopiją

# Setų aritmetika

union:

```python
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.union(x2)
{'foo', 'qux', 'quux', 'baz', 'bar'}

>>> x1 | x2
{'foo', 'qux', 'quux', 'baz', 'bar'}
```

intersection:

```python
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.intersection(x2)
{'baz'}

>>> x1 & x2
{'baz'}
```

difference (return the set of all elements that are in x1 but not in x2):

```python
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.difference(x2)
{'foo', 'bar'}

>>> x1 - x2
{'foo', 'bar'}
```

symetric difference (return the set of all elements in either x1 or x2, but not both):

```python
>>> x1 = {'foo', 'bar', 'baz'}
>>> x2 = {'baz', 'qux', 'quux'}

>>> x1.symmetric_difference(x2)
{'foo', 'qux', 'quux', 'bar'}

>>> x1 ^ x2
{'foo', 'qux', 'quux', 'bar'}
```
