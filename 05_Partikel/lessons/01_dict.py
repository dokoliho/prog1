dictionary = { "Haus": "house", "Baum": "tree", "Auto": "car" }
print(dictionary["Haus"]) # house

if "Baum" in dictionary:
    print(f"Baum ist im Wörterbuch enthalten -> {dictionary['Baum']}")

dictionary["Haus"] = "home"


dictionary["Katze"] = "cat"

