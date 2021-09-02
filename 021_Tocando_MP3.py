# 021_Tocando_MP3.py

import pygame

pygame.init()
pygame.mixer.music.load("A_Singular_Perversion_-_Darkness_-_Kevin_MacLeod.mp3")
pygame.mixer.music.play()
pygame.event.wait()
