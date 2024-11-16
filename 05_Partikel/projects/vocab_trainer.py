import random

class VocabTrainer:
    def __init__(self):
        self.vocab = {}

    def start(self):
        while True:
            selection = self.menu_selection()
            if selection == 1:
                self.add_word()
            elif selection == 2:
                self.show_question()
            else:
                print("Auf Wiedersehen!")
                break

    def menu_selection(self):
        result = None
        while result not in ["1", "2", "3"]:
            print("1. Neues Wort hinzufügen")
            print("2. Wort abfragen")
            print("3. Beenden")
            result = input("Auswahl (1-3): ")
        return int(result)

    def add_word(self):
        foreign = input("Wort in der Fremdsprache: ")
        german = input("Wort auf Deutsch: ")
        self.vocab[foreign] = german

    def show_question(self):
        if len(self.vocab) == 0:
            print("Keine Wörter vorhanden.")
            return
        foreign = random.choice(list(self.vocab.keys()))
        german = self.vocab[foreign]
        answer = input(f"Was bedeutet '{foreign}' auf Deutsch? ")
        if answer == german:
            print("Richtig!")
        else:
            print(f"Falsch! Die richtige Antwort ist '{german}'.")


trainer = VocabTrainer()
trainer.start()