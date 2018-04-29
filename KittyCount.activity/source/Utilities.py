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
    def show_error(screen, error_text):
        # shows helpful errors

        w, h = Utilities.get_width_height()
        x, y = (w/2, h/2 + 120)
        pygame.draw.rect(screen, (255, 255, 255), (x-250, y, 500, 20), 0)
        text_surface = Utilities.make_text_surface(error_text, 16)
        text_size = text_surface.get_size()
        x = x - (text_size[0] / 2)

        screen.blit(text_surface, (x, y))
