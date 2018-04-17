import pygame
import random


class Character:

    displayImage = ""  # path to the image file to be displayed
    imageHeight = 10  # height of the image
    imageWidth = 10  # width of the image
    screen = 0  # screen to display on
    positions = []  # array of circle positions
    x = 0  # x position of character
    y = 0  # y position of character

    def __init__(self, _positions, _display_image, _image_height, _image_width, screen, other_character_x=-1):
        self.positions = _positions
        self.displayImage = _display_image
        self.imageHeight = _image_height
        self.imageWidth = _image_width
        self.screen = screen
        self.img = pygame.image.load(self.displayImage)
        self.set_position(other_character_x)

    def get_x_pos(self):
        return self.x

    def get_y_pos(self):
        return self.y

    def set_x_pos(self, _x):
        self.x = _x

    def set_y_pos(self, _y):
        self.y = _y

    def set_image_height(self, _image_height):
        self.imageHeight = _image_height

    def set_image_width(self, _image_width):
        self.imageWidth = _image_width
    
    def set_position(self, _other_character_x):
        rand = random.randint(0, (len(self.positions) - 1))
        valid = False
        
        while not valid:
            x, y = self.positions[rand]
            self.set_x_pos(x - (self.imageWidth / 2))
            self.set_y_pos(y - (self.imageHeight + 20))
            print(x)
            if x != _other_character_x:
                valid = True

    def display(self):
        self.screen.blit(pygame.transform.scale(self.img, (self.imageHeight, self.imageWidth)), (self.x, self.y))

