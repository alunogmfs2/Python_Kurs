operationen = ["Addieren", "Subtrehieren", "Multiplizieren", "Dividieren"]

while True:
    for i, op in enumerate(operationen):
        print(f'{i+1} - {op}')
    print("0 - Ende")

    antwort = int(input("Was willst du? "))
    if antwort != 0:
        antwort = operationen[antwort - 1]

        n1 = int(input("Zahl 1: "))
        n2 = int(input("Zahl 2: "))

    # print(antwort)

    if not (antwort in operationen) and antwort != 0:
        print("Schreiben Sie eine gueltige Option")

    match antwort:
        case "Addieren":
            print(f'{n1} + {n2} = {n1 + n2}')
        case "Subtrehieren":
            print(f'{n1} - {n2} = {n1 - n2}')
        case "Multiplizieren":
            print(f'{n1} * {n2} = {n1 * n2}')
        case "Dividieren":
            print(f'{n1} / {n2} = {n1 / n2}')
        case 0:
            print("Ende")
            break
