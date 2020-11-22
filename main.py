import json


class Item:
    def __init__(self, zmienna, nazwa):
        self.zmienna = zmienna
        self.nazwa = nazwa

    def __str__(self):
        return str('{' + f'"{self.zmienna}":"{self.nazwa}"' + '}')

    def func(self):
        return str('{' + f'"{self.zmienna}":"{self.nazwa}"' + '}')


def check_par(klasa):
    counter = 0
    nr = 0
    tab = []
    for linia in klasa:
        if 'class' in linia and counter == 0:
            var = linia.split(' ')[1].rstrip(':')
        if '{' in linia:
            counter += 1
        if '}' in linia:
            counter -= 1
        nr += 1
        if counter == 1:
            if 'displayname' in linia:
                nazwa = linia.split('"')[1]
                obj = Item(var, nazwa)
                tab.append(obj.func())
    return tab


with open('cfgWeapons.txt') as f:
    parsed = ''
    returnedList = check_par(f)

out = json.dumps(returnedList)

with open('output.json', 'w+') as f:
    f.write(out)
