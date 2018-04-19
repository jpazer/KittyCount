import pygame
<<<<<<< HEAD
from game.Utilities import Utilities
from game.UI import UI
=======
from source.GameController import GameController

>>>>>>> development

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    # screen = pygame.display.set_mode((0, 0))  # windowed app for DEV only
    screen.fill((255, 255, 255))
    done = False

    game_controller = GameController(screen)

<<<<<<< HEAD

    clock = pygame.time.Clock()
    # exit logic
=======
>>>>>>> development
    while not done:
        events = pygame.event.get()
<<<<<<< HEAD
=======

        game_controller.loop(events)

>>>>>>> development
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = True

<<<<<<< HEAD
        
        # draw UI
        screen.fill((255, 255, 255))
        ui.display(events)
        

=======
>>>>>>> development
        pygame.display.update()
        clock.tick(30)


if __name__ == '__main__':
    main()
