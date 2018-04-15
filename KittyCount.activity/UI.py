from UserInput import UserInput
from Button import Button


class UI:

    def __init__(self, screen, x, y):
        # make UI
        self.user_input = UserInput(screen, (x + 108, y + 20))

        # make button
        def add():
            return 0

        self.button_add = Button(screen, (x + 280, y), (80, 90), "+", 80, add())

        def sub():
            return 0

        self.button_sub = Button(screen, (x, y), (80, 90), "-", 80, sub())

        def submit():
            return 0

        self.button_go = Button(screen, (x + 118, y + 95), (370, 70), "Go", 60, submit())

    def display(self, events):
        # draw UI
        self.user_input.display(events)

        # draw button
        self.button_add.display(events)
        self.button_sub.display(events)
        self.button_go.display(events)

