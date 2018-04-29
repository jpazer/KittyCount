import pygame
from source.NumberCircle import NumberCircle
from source.Utilities import Utilities


class NumberLine:
    num_of_points = 20  # num of points on number line
    circle_pos = []
    circles = []
    level = 1

    def __init__(self, screen, w, h):
        self.screen = screen
        self.number_line_y = int(h / 2)  # y of where number line is drawn
        self.spacing = int((w - 100) / self.num_of_points)  # in pixels
        self.start_x = int(self.spacing / 2) + 50  # x where the first point is and the number line starts
        self.end_x = int(w - self.spacing / 2) - 50  # x where the last point is and the number line ends

        self.make_circles()

    def make_circles(self):
        # draw points on line
        for num in range(0, 20):
            position = (self.start_x + num * self.spacing, self.number_line_y)
            self.circle_pos.append(position)
            circle = NumberCircle(self.screen, position)
            self.circles.append(circle)

    def display_circles(self):
        # draw points on line
        for num in range(0, 20):
            self.circles[num].display()

    def display_numbers(self):
        for num in range(0, len(self.circle_pos)):
            # draw number beneath circle
            x = self.circle_pos[num][0] - 5
            y = self.circle_pos[num][1] + 15
            text_surface = Utilities.make_text_surface(str(num * self.level), 20)
            text_size = text_surface.get_size()
            x = x - (text_size[0]/4)
            self.screen.blit(text_surface, (x, y))

    def clear_numbers(self):
        # cover over numbers
        pygame.draw.rect(self.screen, (255, 255, 255), (0, self.number_line_y + 10,
                                                        Utilities.get_width_height()[0], 30), 0)

    def display(self):
        # draw line
        pygame.draw.line(self.screen, (0, 0, 0), (self.start_x, self.number_line_y), (self.end_x, self.number_line_y))
        self.display_circles()
        self.display_numbers()

    def change_level(self, level):
        self.level = level
        self.clear_numbers()
        self.display_numbers()
