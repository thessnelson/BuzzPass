import pygame
import pygame_menu
import os
import time
from pygame.color import Color
from RPi import GPIO

pygame.init()
surface = pygame.display.set_mode((128, 128))
menu = pygame_menu.Menu('Juan', 128, 128, theme=pygame_menu.themes.THEME_DARK)

def set_file(file, index):
    #We get to list out the files necessary for sending
    pass

def send():
    #encrypt
    #communicate
    #send
    pass

def receive():
    #decrypt
    #communicate
    #receive
    pass

menu.add.selector('File :', [('NavySeals.txt', 1), ('Wyoming.txt', 2)], onchange=set_file)
menu.add.button('Send', send)
menu.add.button('Listen', receive)
menu.add.button('Exit', pygame_menu.events.EXIT)

menu.mainloop(surface)