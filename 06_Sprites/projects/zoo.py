import random

class Animal:
    def __init__(self):
        self.name = None
        self.species = None
        self.age = None

    def __str__(self):
        return f"Name: {self.name}, Art: {self.species}, Alter: {self.age}"

    def make_sound(self):
        print("")

    def init_by_input(self):
        self.name = input("Name: ")
        self.species = input("Art: ")
        self.age = int(input("Alter: "))


class Bird(Animal):
    def __str__(self):
        return f"Vogel - {super().__str__()}"

    def make_sound(self):
        print("Chirp chirp")


class Mammal(Animal):
    def __str__(self):
        return f"Säugetier - {super().__str__()}"

    def make_sound(self):
        print("Roar")







def main():
    zoo_animals = []
    while True:
        choice = show_menue()
        if choice == "1":
            zoo_animals.append(new_bird())
        elif choice == "2":
            zoo_animals.append(new_mammal())
        elif choice == "3":
            list_animals(zoo_animals)
        elif choice == "4":
            concert(zoo_animals)
        elif choice == "5":
            print("Programm wird beendet. Auf Wiedersehen!")
            break
        else:
            print("Ungültige Eingabe. Bitte versuchen Sie es erneut.\n")


def show_menue():
    print("Zoo-Menü:")
    print("1. Neuen Vogel hinzufügen")
    print("2. Neues Säugetier hinzufügen")
    print("3. Alle Tiere auflisten")
    print("4. Konzert der Tiere")
    print("5. Beenden")
    choice = input("Wählen Sie eine Option: ")
    return choice


def new_bird():
    bird = Bird()
    print("Geben Sie die Daten des Vogels ein:")
    bird.init_by_input()
    return bird


def new_mammal():
    mammal = Mammal()
    print("Geben Sie die Daten des Säugetiers ein:")
    mammal.init_by_input()
    return mammal


def list_animals(lst):
    if len(lst)==0:
        print("Es gibt noch keine Tiere im Zoo.\n")
    else:
        print("Liste der Tiere im Zoo:")
        for animal in lst:
            print(animal)
        print()


def concert(lst):
    if len(lst)==0:
        print("Es gibt keine Tiere für ein Konzert.\n")
    else:
        print("Konzert der Tiere:")
        random.shuffle(lst)
        for animal in lst:
            print(f"{animal.name} ({animal.species}):")
            animal.make_sound()
        print()


if __name__ == "__main__":
    main()
