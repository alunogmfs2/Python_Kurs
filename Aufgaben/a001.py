personen = []

while True:
    person = []
    name = input('Name: ')
    alter = input('Alter: ')
    geschlecht = input('Geschlecht [M/W]: ').lower()

    person.append(name)
    person.append(alter)
    person.append(geschlecht)

    personen.append(person)

    weiter = input('Wollen Sie noch jemand registrieren [J/N] ? ').lower()

    if weiter != 'j':
        break

print()

for p in personen:
    print('Hallo', p[0])
    print('Sie sind', p[1], 'Jahre alt')

    if p[2] == 'm':
        print('Sie sind männlich')
    else:
        print('Sie sind weiblich')

    print()
