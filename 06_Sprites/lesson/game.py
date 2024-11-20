import pygame

# Festlegung der Konstanten
WIDTH = 640
HEIGHT = 400
SIZE = (WIDTH, HEIGHT)
FPS = 60
BLACK = (0, 0, 0)


class Game:

    # Konstruktor
    def __init__(self, title, fps=FPS, size=SIZE):
        self.title = title
        self.fps = fps
        self.size = size
        self.screen = self.init_game()
        self.clock = pygame.time.Clock()

    def run(self):
        self.init_game()
        self.game_loop()
        self.exit_game()

    # Initialisierung von Pygame
    def init_game(self):
        pygame.init()
        pygame.display.set_caption(self.title)
        screen = pygame.display.set_mode(self.size)
        self.init_game_state()
        return screen

    # Initialisierung des Spielzustands
    # Sollte in abgeleiteten Klassen überschrieben werden
    def init_game_state(self):
        pass

    # Game-Loop mit Standardstruktur
    def game_loop(self):
        while True:
            # Berechnung der Zeitdifferenz seit dem letzten Frame in Sekunden
            self.dt = self.clock.tick(self.fps) / 1000
            if self.event_handling() == False:
                break
            if self.update_game() == False:
                break
            self.draw_game()

    # Beenden von Pygame
    def exit_game(self):
        pygame.quit()

    # Event-Behandlung
    def event_handling(self):
        for event in pygame.event.get():
            if not self.handle_event(event):
                return False
        return True

    # Behandlung eines Events
    # Sollte in abgeleiteten Klassen überschrieben werden
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            return False
        return True

    # Aktualisierung des Spiels
    # Sollte in abgeleiteten Klassen überschrieben werden
    def update_game(self):
        return True

    # Zeichnen des Spiels
    # Sollte in abgeleiteten Klassen überschrieben werden
    def draw_game(self):
        self.screen.fill(BLACK)
        pygame.display.flip()
