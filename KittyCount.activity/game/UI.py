from game.UserInput import UserInput
from game.Button import Button
from game.Utilities import Utilities
from game.NumberLine import NumberLine
from game.character import *

class UI:

    def __init__(self, screen, x, y):
        # make UI
        w, h = Utilities.get_width_height()
        self.user_input = UserInput(screen, (x + 108, y + 20))
        self.button_add = Button(screen, (x + 280, y), (80, 90), "+", 80, self.add, self.user_input)
        self.button_sub = Button(screen, (x, y), (80, 90), "-", 80, self.sub, self.user_input)
        self.button_go = Button(screen, (x + 118, y + 95), (370, 70), "Go", 60, self.submit, self.user_input)
        self.number_line = NumberLine(screen, w, h)
        self.cat = character(self.number_line.circle_pos[7][0], self.number_line.circle_pos[7][1], "../Assets/cat1.png", 100, 100, screen)
        self.mouse = character (self.number_line.circle_pos[3][0], self.number_line.circle_pos[3][1], "../Assets/mouse3.png", 50, 50, screen)

    def display(self, events):
        # draw UI
        self.user_input.display(events)
        self.cat.display()
        self.mouse.display()
        self.number_line.display()
        # draw button
        self.button_add.display(events)
        self.button_sub.display(events)
        self.button_go.display(events)

    def submit(self, screen, user_input):
        Utilities.show_error(screen, str(user_input.get_input()))
        multiplier = int(user_input.get_input())
        self.cat.move(self.number_line.spacing * multiplier)

    # make button
    def add(self, screen, user_input):
        user_input.add(1)

    def sub(self, screen, user_input):
        user_input.add(-1)