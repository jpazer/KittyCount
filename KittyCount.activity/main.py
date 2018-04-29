import pygame
from source.GameController import GameController


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    #screen = pygame.display.set_mode((0, 0))  # windowed app for DEV only
    screen.fill((255, 255, 255))
    done = False

    game_controller = GameController(screen)

    clock = pygame.time.Clock()

    while not done:
        events = pygame.event.get()

        game_controller.loop(events)

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
