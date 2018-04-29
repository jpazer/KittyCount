from source.Button import Button
from source.Utilities import Utilities


class EndScreen:
    def __init__(self, screen, message):
        x, y = Utilities.get_width_height()
        self.screen = screen
        self.restart = Button(screen, ((x/2)-350, y/2), (300, 100), "Restart", 50, 4)
        self.quit = Button(screen, ((x/2)+50, y/2), (300, 100), "Quit", 50, 5)
        self.message = Utilities.make_text_surface(message, 60)

        self.message_width = self.message.get_rect().width

    def display(self, events):
        self.screen.fill((255, 255, 255))

        x, y = Utilities.get_width_height()
        self.restart.display(events)
        self.quit.display(events)
        self.screen.blit(self.message, ((x/2)-(self.message_width/2), (y/2)-150))




