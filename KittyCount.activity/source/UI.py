import pygame
from source.UserInput import UserInput
from source.Button import Button
from source.Utilities import Utilities
from source.EndScreen import EndScreen


class UI:

    def __init__(self, screen, x, y):
        # make UI
        ui_width = 370
        ui_height = 160
        x = x - ui_width/2

        self.button_sub = Button(screen, (x, y), (80, (ui_height*0.56)), "-", 80, 2)
        self.user_input = UserInput(screen, (x + 85, y), 200, ui_height*0.56)
        self.button_add = Button(screen, (x + 290, y), (80, (ui_height*0.56)), "+", 80, 1)
        self.button_go = Button(screen, (x, y + 95), (ui_width, (ui_height*0.44)), "Go", 60, 3)
        self.screen = screen
        self.EndScreen = EndScreen(screen, "YOU WIN")

    def display(self, events, end):
        if not end:
            # draw UI
            self.user_input.display(events)

            # draw button
            self.button_add.display(events)
            self.button_sub.display(events)
            self.button_go.display(events)
        else:
            self.EndScreen.display(events)

    def update_level(self, level):
        # display level
        pygame.draw.rect(self.screen, (255, 255, 255), (10, 10, 200, 50), 0)
        self.screen.blit(Utilities.make_text_surface("Level: " + str(level), 30), (10, 10))
