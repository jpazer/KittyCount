import pygame
import random

class character:
    displayImage = "" #path to the image file to be displayed
    imageHeight = 10 #height of the image
    imageWidth= 10 #width of the image
    screen = 0 #screen to display on
    positions = [] # array of circle positions
    xPos = 0 #x position of character
    yPos = 0 #y position of character

    def __init__(self, _positions,_displayImage, _imageHeight, _imageWidth, screen, otherCharacterX = -1):
        self.positions = _positions
        self.displayImage = _displayImage
        self.imageHeight = _imageHeight
        self.imageWidth = _imageWidth
        self.screen = screen
        self.img = pygame.image.load(self.displayImage)
        self.setPosition(otherCharacterX)


    def getxPos(self):
        return self.xPos

    def getyPos(self):
        return yPos

    def setxPos(self, _xPos):
        self.xPos = _xPos

    def setyPos(self, _yPos):
        self.yPos = _yPos

    def setImageHeight(_imageHeight):
        self.imageHeight = _imageHeight

    def setImageWidth(_imageWidth):
        self.imageWidth = _imageWidth
    
    def setPosition(self, otherCharacterX):
        rand = random.randint(0, (len(self.positions) - 1 ))
        valid = False
        
        while not valid:
            xPos, yPos = self.positions[rand]
            self.setxPos(xPos - (self.imageWidth / 2) )
            self.setyPos(yPos - (self.imageHeight + 20))
            print (xPos)            
            if xPos != otherCharacterX:
                valid = True


    def display(self):
        self.screen.blit(pygame.transform.scale(self.img, (self.imageHeight,self.imageWidth)),(self.xPos,self.yPos))

