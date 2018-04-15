import pygame
from NumberCircle import NumberCircle



class NumberLine:
    num_of_points = 20  # num of points on number line

    def __init__(self,screen, w, h):
        self.screen = screen

        self.number_line_y = int(h / 2)  # y of where number line is drawn
        self.spacing = int(w / self.num_of_points)  # in pixels
        self.start_x = int(self.spacing / 2)  # x there the first point is and the number line starts
        self.end_x = int(w - self.spacing / 2)  # x where the last point is and the number line ends

    def display(self):
        # draw line
        pygame.draw.line(self.screen, (0, 0, 0), (self.start_x, self.number_line_y), (self.end_x, self.number_line_y))

        # draw points on line
        for num in range(0, 20):
            number = str(num)
            position = (self.start_x + num * self.spacing, self.number_line_y)
            circle = NumberCircle(position, number, self.screen)
            circle.display()