notes = input("Введите номера нот через пробел: ").split()

for note in notes:
    note = int(note)
    if note == 1 or note == 4:
        print("# до", end=" ")
    elif note == 2 or note == 5:
        print("# ре", end=" ")
    elif note == 3:
        print("ми", end=" ")
    elif note == 6:
        print("фа", end=" ")
    elif note == 7:
        print("# фа", end=" ")

print()
