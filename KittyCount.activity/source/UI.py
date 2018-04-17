import pygame
from source.UserInput import UserInput
from source.Button import Button
from source.Utilities import Utilities


class UI:

    def __init__(self, screen, x, y):
        # make UI
        self.user_input = UserInput(screen, (x + 108, y + 20))
        self.button_add = Button(screen, (x + 280, y), (80, 90), "+", 80, "add")
        self.button_sub = Button(screen, (x, y), (80, 90), "-", 80, "sub")
        self.button_go = Button(screen, (x + 118, y + 95), (370, 70), "Go", 60, "go")
        self.screen = screen

    def display(self, events):
        # draw UI
        self.user_input.display(events)

        # draw button
        self.button_add.display(events)
        self.button_sub.display(events)
        self.button_go.display(events)

        for event in events:
            if event.type == pygame.USEREVENT:
                if event.button_type == "add":
                    self.user_input.add(1)
                if event.button_type == "sub":
                    self.user_input.add(-1)

