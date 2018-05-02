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

        w, h = Utilities.get_width_height()

        # shows helpful errors
        w, h = Utilities.get_width_height()
        x, y = (w/2, h/2 + 100)

        pygame.draw.rect(screen, (255, 255, 255), (x-250, y, 500, 20), 0)
        text_surface = Utilities.make_text_surface(error_text, 16)
        text_size = text_surface.get_size()
        x = x - (text_size[0] / 2)

        screen.blit(text_surface, (x, y))

    @staticmethod
    # draw some text into an area of a surface
    # automatically wraps words
    # returns any text that didn't get blitted
    def draw_text(screen, text, rect, size=12, color=(0, 0, 0), aa=False, bkg=None):
        font = pygame.font.SysFont('arial', size)
        rect = pygame.Rect(rect)
        y = rect.top
        line_spacing = 2

        # get the height of the font
        font_height = font.size("Tg")[1]

        while text:
            i = 1

            # determine if the row of text will be outside our area
            if y + font_height > rect.bottom:
                break

            # determine maximum width of line
            while font.size(text[:i])[0] < rect.width and i < len(text):
                i += 1

            # if we've wrapped the text, then adjust the wrap to the last word
            if i < len(text):
                i = text.rfind(" ", 0, i) + 1

            # render the line and blit it to the surface
            if bkg:
                image = font.render(text[:i], 1, color, bkg)
                image.set_colorkey(bkg)
            else:
                image = font.render(text[:i], aa, color)

            screen.blit(image, (rect.left-rect.width/2, y))
            y += font_height + line_spacing

            # remove the text we just blitted
            text = text[i:]

        return text
