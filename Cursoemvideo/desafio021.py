""" pygame importar """
import pygame
pygame.init()
# chamando a musica/exportando a musica para o python
pygame.mixer.music.load('Akumatizados3.mp3')
# play na musica
pygame.mixer.music.play()
input()
pygame.event.wait()
