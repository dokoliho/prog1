class Vehicle:
    def __init__(self, brand, model, year, milage):
        self.brand = brand
        self.model = model
        self.year = year
        self.milage = milage

    def __str__(self):
        return f"{self.brand} {self.model}, Baujahr: {self.year}, Kilometerstand: {self.milage} km"

    def init_by_input(self):
        self.brand = input("Marke: ")
        self.model = input("Model: ")
        self.year = int(input("Baujahr: "))
        self.milage = float(input("Kilometerstand (in km): "))


class Car(Vehicle):
    def __init__(self, brand=None, model=None, year=None, milage=None, num_doors=None):
        super().__init__(brand, model, year, milage)
        self.num_doors = num_doors

    def __str__(self):
        return f"{super().__str__()}, Türen: {self.num_doors}"

    def init_by_input(self):
        super().init_by_input()
        self.num_doors = int(input("Anzahl Türen: "))


class Truck(Vehicle):
    def __init__(self, brand=None, model=None, year=None, milage=None, load_capacity=None):
        super().__init__(brand, model, year, milage)
        self.load_capacity = load_capacity

    def __str__(self):
        return f"{super().__str__()}, Zuladung: {self.load_capacity}"

    def init_by_input(self):
        super().init_by_input()
        self.load_capacity = float(input("Zuladung (in Tonnen): "))


def main():
    fleet = []

    while True:
        choice = show_menu()
        if choice == "1":
            car = Car()
            car.init_by_input()
            fleet.append(car)
            print("Auto erfolgreich hinzugefügt!")

        elif choice == "2":
            truck = Truck()
            truck.init_by_input()
            fleet.append(truck)
            print("LKW erfolgreich hinzugefügt!")

        elif choice == "3":
            show_fleet(fleet)

        elif choice == "4":
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Eingabe, bitte erneut versuchen.")


def show_fleet(fleet):
    if len(fleet) == 0:
        print("Keine Fahrzeuge im Fuhrpark.")
    else:
        print("Fuhrpark:")
        for vehicle in fleet:
            print(vehicle)


def show_menu():
    print("\nFuhrparkverwaltung")
    print("1. Hinzufügen eines neuen Autos")
    print("2. Himzufügen eines neuen LKW")
    print("3. Anzeigen aller Fahrzeuge")
    print("4. Programm beenden")
    choice = input("Ihre Wahl: ")
    return choice


if __name__ == "__main__":
    main()
