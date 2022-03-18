import pygame

pygame.init()

win = pygame.display.set_mode((400,500))
pygame.display.set_caption("Geeky Game for Geeks")
icon = pygame.image.load('word.png')
pygame.display.set_icon(icon)

running = True
while running == True:
    # win.fill(white)
    win.blit(icon, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        pygame.display.update()