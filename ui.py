import pygame
import pygame_menu
import os
import time
from pygame.color import Color
#import RPi.GPIO as GPIO
'''
joystick left increments selector index in set_file
joystick right decrements selector index in set_file
key1 sends file
key2 listens for file
key3 exits when pressed twice

pinout via waveshare site: https://www.waveshare.com/1.44inch-lcd-hat.htm
key1: Pin 21
key2: Pin 20
key3: Pin 16

JoystickLeft: Pin 5
JoystickRight: Pin 26
'''

pygame.init()
surface = pygame.display.set_mode((300, 300))
menu = pygame_menu.Menu(height=300, width=300, title = 'Juan', theme=pygame_menu.themes.THEME_DARK)

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

menu.add.selector('File :', [('NavySeals.txt', 1), ('Wyoming.txt', 2), ('DoinYourMom.txt', 2)], onchange=set_file)
menu.add.button('Send', send)
menu.add.button('Listen', receive)
menu.add.button('Exit', pygame_menu.events.EXIT)

clock = pygame.time.Clock()
isRunning = True
'''
while isRunning == True:
    time = clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            isRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                isRunning = False
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == 0:
                print('Key1 pressed')
                send()
            if event.button == 1:
                print('Key2 pressed')
                receive()
            if event.button == 2:
                print('Key3 pressed')
                isRunning = False
'''
menu.mainloop(surface)