import pygame
from NumberCircle import NumberCircle
from Utilities import Utilities
from UserInput import UserInput
from Button import Button

from pygame.locals import *


def main():
    pygame.init()
    pygame.font.init()

    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((0, 0))  # windowed app for DEV only
    screen.fill((255, 255, 255))
    pygame.display.flip()
    done = False

    # setup variables
    w, h = Utilities.get_width_height()  # width and height of the screen

    number_line_y = int(h/2)  # y of where number line is drawn
    num_of_points = 20  # num of points on number line
    spacing = int(w/num_of_points)  # in pixels
    start_x = int(spacing/2) # x there the first point is and the number line starts
    end_x = int(w-spacing/2) # x where the last point is and the number line ends

    # draw line
    pygame.draw.line(screen, (0, 0, 0), (start_x, number_line_y), (end_x, number_line_y))

    # draw points on line
    for num in range(0, 20):
        number = str(num)
        position = (start_x + num * spacing, number_line_y)
        circle = NumberCircle(position, number, screen)
        circle.display()

    # make UI
    user_input = UserInput(screen, (w/2 - 100, h-200))

    # make button
    def add():
        return 0

    button_add = Button(screen, (w/2 + 100, h-220), (70, 70), add(), "+", 80)

    def sub():
        return 0

    button_sub = Button(screen, (w / 2 - 250, h - 220), (70, 70), sub(), "-", 80)


    # exit logic
    while not done:
        x, y = screen.get_size()
        clock = pygame.time.Clock()
        events = pygame.event.get()

        # draw UI
        user_input.display(events)

        #draw button
        button_add.display(events)
        button_sub.display(events)

        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True


        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
