with open("Datei.txt", "w") as f:
    f.write("Nürnberg ist schön!\n")
    f.write("Fürth geht so.")

with open("Datei.txt", "r") as f:
    print(f.read())

print("\u2764")