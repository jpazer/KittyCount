import pygame

class character:
    xPos = 0 #the x coordinate of the cat image
    yPos = 0 #the y coordinate of the cat image
    displayImage = "" #path to the image file to be displayed
    imageHeight = 10 #height of the image
    imageWidth= 10 #width of the image
    screen = 0 #screen to display on
    
    def __init__(self, _xPos, _yPos,_displayImage, _imageHeight, _imageWidth, screen):
        self.xPos = _xPos
        self.yPos = _yPos
        self.displayImage = _displayImage
        self.imageHeight = _imageHeight
        self.imageWidth = _imageWidth
        self.screen = screen
        self.img = pygame.image.load(self.displayImage)
    def getxPos():
        return self.xPos

    def getyPos():
        return yPos

    def setxPos(_xPos):
        self.xPos = _xPos

    def setyPos(_yPos):
        self.yPos = _yPos

    def setImageHeight(_imageHeight):
        self.imageHeight = _imageHeight

    def setImageWidth(_imageWidth):
        self.imageWidth = _imageWidth

    def display(self):
        y = (self.yPos - self.imageHeight - 20)
        x = (self.xPos - (self.imageWidth / 2))
        self.screen.blit(pygame.transform.scale(self.img,(self.imageHeight,self.imageWidth)),(x,y))
    def move(self, x):
        self.xPos += 20
        


