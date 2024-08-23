while True:
    geschlecht = input("[M/W]: ").lower()
    if geschlecht != "m" and geschlecht != "w":
        print("Fehler")
        print("\n" * 30)
    else:
        break
