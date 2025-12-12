import random

FILENAME = "vocab.txt"

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
            elif selection == 3:
                self.save_vocab()
            elif selection == 4:
                self.load_vocab()
            else:
                print("Auf Wiedersehen!")
                break

    def menu_selection(self):
        result = None
        while result not in [str(i) for i in range(1, 6)]:
            print("1. Neues Wort hinzufügen")
            print("2. Wort abfragen")
            print("3. Wörterbuch speichern")
            print("4. Wörterbuch laden")
            print("5. Beenden")
            result = input("Auswahl (1-5): ")
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

    def save_vocab(self):
        with open(FILENAME, "w") as f:
            for foreign, german in self.vocab.items():
                f.write(f"{foreign}\n{german}\n")

    def load_vocab(self):
        with open(FILENAME, "r") as f:
            lines = f.readlines()
            self.vocab = {}
            for i in range(0, len(lines), 2):
                foreign = lines[i].strip()
                german = lines[i + 1].strip()
                self.vocab[foreign] = german

trainer = VocabTrainer()
trainer.start()