import pygame
from Utilities import Utilities
from UI import UI
from NumberLine import NumberLine


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


    # display UI
    ui = UI(screen, w/2 - 200, h/2 + 150)

    #display Number Line
    number_line = NumberLine(screen, w, h)
    number_line.display()


    # exit logic
    while not done:
        clock = pygame.time.Clock()
        events = pygame.event.get()

        # draw UI
        ui.display(events)

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
