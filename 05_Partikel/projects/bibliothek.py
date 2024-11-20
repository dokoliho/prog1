class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"'{self.title}' von {self.author} ({self.year})"

class LibraryManager:
    def __init__(self):
        # Dictionary zum Speichern der Bücher
        self.library = {}

    def start(self):
        while True:
            print("\nBibliotheks-Manager")
            print("1. Buch hinzufügen")
            print("2. Buch suchen")
            print("3. Alle Bücher anzeigen")
            print("4. Beenden")
            choice = input("Auswahl (1-4): ")

            if choice == "1":
                self.add_book()
            elif choice == "2":
                self.search_book()
            elif choice == "3":
                self.display_all_books()
            elif choice == "4":
                print("Programm beendet.")
                break
            else:
                print("Ungültige Eingabe, bitte erneut versuchen.")

    def add_book(self):
        title = input("Geben Sie den Titel des Buches ein: ")
        author = input("Geben Sie den Autor des Buches ein: ")
        year = input("Geben Sie das Erscheinungsjahr ein: ")

        # Prüfen, ob das Buch bereits existiert
        if title in self.library:
            print(f"Das Buch '{title}' ist bereits in der Bibliothek.")
        else:
            self.library[title] = Book(title, author, year)
            print(f"Das Buch '{title}' wurde hinzugefügt.")

    def search_book(self):
        title = input("Geben Sie den Titel des Buches ein: ")
        if title in self.library:
            print(self.library[title])  # __str__ der Klasse Book wird aufgerufen
        else:
            print(f"Das Buch '{title}' wurde nicht gefunden.")

    def display_all_books(self):
        if not self.library:
            print("Die Bibliothek ist leer.")
        else:
            print("Liste aller Bücher:")
            for title in self.library:
                print(f"- {title}")


library = LibraryManager()
library.start()
