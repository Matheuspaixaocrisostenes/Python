'''import pygame
pygame.init()
pygame.mixer.music.play()
pygame.event.wait()'''
import emoji
from pygame import mixer
mixer.init()
pygame.mixer.music.load('nome da musica vai aqui baixe um arquivo .mp3 e coloque aqui')
mixer.music.play()
print(emoji.emojize("Hello world :heart: ",use_aliases=True))
input('Teste com musica')
print(emoji.emojize("5 :heart: ",use_aliases=True))
