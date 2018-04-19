import pygame


class Utilities:

    fake_num = (0, 0)

    def __init__(self):
        return

    @staticmethod
    def make_text_surface(text, size=12):
        # makes it faster to print text to screen
        font = pygame.font.SysFont('arial', size)
        text_surface = font.render(text, False, (0, 0, 0))
        return text_surface

    @staticmethod
    def get_width_height():
        # get the w and h of the full screen
        return pygame.display.get_surface().get_size()

    @staticmethod
    def show_error(screen, error_text, position=(10, 10)):
        # shows helpful errors (not yet implemented)
        screen.blit(Utilities.make_text_surface(error_text, 12), position)
