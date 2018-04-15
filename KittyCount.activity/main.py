import pygame
from Utilities import Utilities
from UI import UI
from NumberLine import NumberLine
from character import character
import time

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
    #display cat
    cat_x, cat_y = number_line.circle_pos[7]
    cat = character(cat_x, cat_y, "../Assets/cat1.png", 100, 100, screen)

            
    #display mouse
    mouse_x, mouse_y = number_line.circle_pos[3]
    mouse = character (mouse_x, mouse_y, "../Assets/mouse3.png", 50, 50, screen)

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
        number_line.display()
        mouse.display()
        

        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
