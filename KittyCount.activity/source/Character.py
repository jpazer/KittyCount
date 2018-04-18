import pygame
import random


class Character:

    displayImage = ""  # path to the image file to be displayed
    imageHeight = 10  # height of the image
    imageWidth = 10  # width of the image
    screen = 0  # screen to display on
    positions = []  # array of circle positions
    currentPosition = 0
    x = 0  # x position of character
    y = 0  # y position of character

    def __init__(self, _positions, _display_image, _image_height, _image_width, _screen, other_character_x=-1):
        self.positions = _positions
        self.displayImage = _display_image
        self.imageHeight = _image_height
        self.imageWidth = _image_width
        self.screen = _screen


    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def set_x_pos(self, _x):
        self.x = _x

    def set_y_pos(self, _y):
        self.y = _y
    
    def set_display_image(self, _displayImage):
        self.displayImage = _displayImage

    def set_image_height(self, _image_height):
        self.imageHeight = _image_height

    def set_image_width(self, _image_width):
        self.imageWidth = _image_width

    def update_position(self, new_pos):
        self.erase()

        self.currentPosition = new_pos
        x, y = self.positions[self.currentPosition]
        self.set_x_pos(x - (self.imageWidth / 2))
        self.set_y_pos(y - (self.imageHeight + 20))
        self.display()

    def set_random_position(self, _other_character_position):
        rand = random.randint(0, (len(self.positions) - 1))

        if rand != _other_character_position:
            self.update_position(rand)
            return rand
        else:
            self.set_random_position(_other_character_position)

    def display(self):
        self.img = pygame.image.load(self.displayImage)
        self.screen.blit(pygame.transform.scale(self.img, (self.imageHeight, self.imageWidth)), (self.x, self.y))

    def erase(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.x, self.y, self.imageWidth, self.imageHeight), 0)

    def move(self, _num):
        if self.currentPosition + _num >= 0 and self.currentPosition <= len(self.positions):
            self.currentPosition += _num
            self.update_position(self.currentPosition)
            return self.currentPosition

