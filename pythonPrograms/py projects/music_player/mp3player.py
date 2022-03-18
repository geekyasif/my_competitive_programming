import pygame
import sys
white = (255, 255, 255)
pygame.init()
display=pygame.display.set_mode((500,500))
pygame.display.set_caption("Python audio player")
pygame.mixer.music.load("play.mp3")
image = pygame.image.load("../tkinter_tut/logo.png")
pygame.mixer.music.play()
while True:
    display.fill(white)
    display.blit(image, (0, 0))

    for eve in pygame.event.get():
            if eve.type==pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            pygame.display.update()