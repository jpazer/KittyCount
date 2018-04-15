import pygame
from game.Utilities import Utilities
from game.UI import UI

def main():
    pygame.init()
    pygame.font.init()

    #screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    screen = pygame.display.set_mode((0, 0))  # windowed app for DEV only
    screen.fill((255, 255, 255))
    done = False

    # setup variables
    w, h = Utilities.get_width_height()  # width and height of the screen


    # display UI
    ui = UI(screen, w/2 - 200, h/2 + 150)


    clock = pygame.time.Clock()
    # exit logic
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

        
        # draw UI
        screen.fill((255, 255, 255))
        ui.display(events)
        

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
