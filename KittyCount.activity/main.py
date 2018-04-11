import pygame
from pygame.locals import *



def main():
	pygame.init()

	screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
	screen.fill((255,255,255))
	pygame.display.flip()
	done = False

	while not done:
		x,y = screen.get_size()
        	for event in pygame.event.get():
                	if event.type == pygame.QUIT:
                    		done = True
                	if event.type == pygame.KEYDOWN:
                    		if event.key == pygame.K_RETURN:
                        		done = True;
        	pygame.draw.line(screen, (0, 0, 0), (x/8, 3*y/4), (7*x/8, 3*y/4))
        	pygame.display.flip()

if  __name__ == '__main__':
	main()
