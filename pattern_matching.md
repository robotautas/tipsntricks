# Pattern matching

Nuo Python 3.10 versijos turime galimybę naudoti ne tik if, bet ir match sąlygas. Abu būdai vienas kitą dubliuoja, tačiau kai kuriuos dalykus daryti patogiau su match.

Tarkime turime funkciją:

```python
def http_error(status):
    if status == 400:
        return "Bad request"
    elif status == 404:
        return "Not found"
    elif status == 418:
        return "I'm a teapot"
    else:
        return "Something's wrong with the internet"
```

šią funkciją galima perrašyti taip:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

taip pat galima naudoti operatorių _|_ kaip "arba":

```python
case 401 | 403 | 404:
    return "Not allowed"
```

įdomiau, kuomet _match'inam_ rinkinius:

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

- kuomet nurodome, kad point yra tuple iš 2jų nulių, suveikia pirmas _case_, kadangi sąlyga pilnai atitinka.

- Sekantis atvejis tikrina atitikimą pagal šabloną (pattern :) ). Jis suveiks, kuomet gaus _tuple_ iš nulio ir bet ko kito. Tą bet ką kitą priskirs kintamąjam y. Jį galėsime panaudoti žemiau sekančioje logikoje.

- _case (x, 0)_ veikia analogiškai.

- _case (x, y)_ . laukia bet kokio tuple iš dviejų narių.

- paskutinis case - default.

Keletas pavyzdžių:

```python
command = 'go north'

match command.split():
    case ["north"] | ["go", "north"]:
        print('going north..')
    case ["get", obj] | ["pick", "up", obj] | ["pick", obj, "up"]:
        print(f'picking {obj}...')
```

galime pirmą _case_ padaryti labiau dinamišku:

```python
match command.split():
    case ["go", ("north" | "south" | "east" | "west") as direction]:
        print(f'going {direction}..')
```

variantas su sekos išpakavimu (sequence unpacking):

```python
match command.split():
    case ["drop", *objects]:
        print("Dropping:")
        for obj in objects:
            print(obj)
```

Taip pat galima įdėti papildomą _if_ saugiklį į sąlygą:

```python
valid_users = ['admin', 'player1', 'player2']

# ...

match command.split():
    case ['sign', 'in', user] if user in valid_users:
        print(f'hello, {user}!')
```

pavyzdžiai su žodynais:

```python
for action in actions:
    match action:
        case {"text": message, "color": c}:
            ui.set_text_color(c)
            ui.display(message)
        case {"sleep": duration}:
            ui.wait(duration)
        case {"sound": url, "format": "ogg"}:
            ui.play(url)
        case {"sound": _, "format": _}:
            warning("Unsupported audio format")
```

žodyne raktas privalo būti literalas, tačiau reikšmė gali būti bet kas (kintamasis, išsireiškimas, etc.).

galimas tipų sutikrinimas:

```python
for action in actions:
    match action:
        case {"text": str(message), "color": str(c)}:
            ui.set_text_color(c)
            ui.display(message)
        case {"sleep": float(duration)}:
            ui.wait(duration)
        case {"sound": str(url), "format": "ogg"}:
            ui.play(url)
        case {"sound": _, "format": _}:
            warning("Unsupported audio format")
```
