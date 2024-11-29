
with open("Datei,txt", "w") as f:
    f.write("Nürnberg ist schön!")

with open("Datei,txt", "r") as f:
    print(f.read())
