from UserInput import UserInput
from Button import Button
from Utilities import Utilities


class UI:

    def __init__(self, screen, x, y):
        # make UI
        self.user_input = UserInput(screen, (x + 108, y + 20))
        self.button_add = Button(screen, (x + 280, y), (80, 90), "+", 80, self.add, self.user_input)
        self.button_sub = Button(screen, (x, y), (80, 90), "-", 80, self.sub, self.user_input)
        self.button_go = Button(screen, (x + 118, y + 95), (370, 70), "Go", 60, self.submit, self.user_input)

    def display(self, events):
        # draw UI
        self.user_input.display(events)

        # draw button
        self.button_add.display(events)
        self.button_sub.display(events)
        self.button_go.display(events)

    def submit(self, screen, user_input):
        Utilities.show_error(screen, str(user_input.get_input()))

    # make button
    def add(self, screen, user_input):
        user_input.add(1)

    def sub(self, screen, user_input):
        user_input.add(-1)