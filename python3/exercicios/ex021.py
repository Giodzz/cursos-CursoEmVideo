import pygame

pygame.mixer.init()
pygame.display.init()
pygame.mixer.music.load("ex021-song.mp3")
pygame.mixer.music.play()
pygame.event.wait()
