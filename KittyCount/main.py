import pygame

pygame.init()

screen = pygame.display.set_mode((640,480))
screen.fill((255,255,255)) 
pygame.display.flip()

done = False

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        done = True;
                        
        pygame.draw.line(screen, (0, 0, 0), (100, 300), (540, 300))
        pygame.display.flip()