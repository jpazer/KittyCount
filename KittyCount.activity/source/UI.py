import pygame
from source.UserInput import UserInput
from source.Button import Button
from source.Utilities import Utilities


class UI:

    def __init__(self, screen, x, y):
        # make UI
        self.x = x
        self.y = y
        self.ui_width = 370
        self.ui_height = 160
        x = x - self.ui_width/2
        w, h = Utilities.get_width_height()
        self.button_sub = Button(screen, (x, y), (80, (self.ui_height*0.56)), "-", 80, 2)
        self.user_input = UserInput(screen, (x + 85, y), 200, self.ui_height*0.56)
        self.button_add = Button(screen, (x + 290, y), (80, (self.ui_height*0.56)), "+", 80, 1)
        self.button_go = Button(screen, (x, y + 95), (self.ui_width, (self.ui_height*0.44)), "Go", 60, 3)
        self.button_quit = Button(screen, (w-110, 10), (100, 50), "Quit", 25, 5)
        self.button_restart = Button(screen, (w-220, 10), (100, 50), "Restart", 25, 4)

        self.screen = screen

    def display(self, events):
            # draw UI
            self.user_input.display(events)

            # draw button
            self.button_add.display(events)
            self.button_sub.display(events)
            self.button_go.display(events)
            self.button_quit.display(events)
            self.button_restart.display(events)


    def update_level(self, level):
        # display level
        pygame.draw.rect(self.screen, (255, 255, 255), (10, 10, 200, 50), 0)
        self.screen.blit(Utilities.make_text_surface("Level: " + str(level), 30), (10, 10))

    def display_all_help_text(self):
        w, h = Utilities.get_width_height()
        self.display_text("Try and catch the mouse!", w/2, 120, 30)
        Utilities.draw_text(self.screen,
                            "Type the number in the box or use the + and - buttons to change it.",
                            (self.x+420, self.y, 320, self.ui_height), 25)
        Utilities.draw_text(self.screen,
                            "Move the cat by telling it how many numbers to jump. " +
                            "Use negative numbers to move backwards.",
                            (self.x-420, self.y, 320, self.ui_height), 25)


    def display_text(self, text, x, y, size):
        text_surface = Utilities.make_text_surface(text, size)
        text_w, text_h = text_surface.get_size()
        self.screen.blit(text_surface, (x - text_w/2, y))
