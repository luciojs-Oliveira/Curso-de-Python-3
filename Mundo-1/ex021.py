#Faça um programa em python que abra e reproduza o áudio de um arquivo mp3.

import pygame
pygame.init()
pygame.mixer.music.load("house_lo.mp3")
pygame.mixer.music.play()
pygame.event.wait()