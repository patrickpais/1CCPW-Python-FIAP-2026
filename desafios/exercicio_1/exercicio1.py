import pygame
import time

pygame.mixer.init()

pygame.mixer.music.load("../sua_musica.mp3")

print ("Reproduzindo áudio... Pressione Ctrl+C para parar.")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    time.sleep(1)