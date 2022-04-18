#library-based
import pygame
import pygame_menu
import os
import time
from pygame.color import Color
import RPi.GPIO as GPIO
import subprocess

#file-based
import LCD_1in44
import LCD_Config

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
KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

pygame.init()
surface = pygame.display.set_mode((128, 128))
menu = pygame_menu.Menu(height=128, width=128, title = 'Juan', theme=pygame_menu.themes.THEME_DARK)

def set_file(index):
    if index == 2:
        send('Wyoming.txt')
    if index == 1:
        send('NavySeals.txt')
    pass

def send(file):
    subprocess.run('./send_file.c')
    pass

def receive():
    subprocess.run('./receive.c')
    pass

def ping():
    subprocess.run('./ping.c')
    pass

menu.add.selector('File :', [('NavySeals.txt', 1), ('Wyoming.txt', 2), ('DoinYourMom.txt', 3)], onchange=set_file)
menu.add.button('Send', send)
menu.add.button('Listen', receive)
menu.add.button('Search', ping)
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
'''
# -*- coding:utf-8 -*-
import LCD_1in44
import LCD_Config

import RPi.GPIO as GPIO

import time
from PIL import Image,ImageDraw,ImageFont,ImageColor

KEY_UP_PIN     = 6 
KEY_DOWN_PIN   = 19
KEY_LEFT_PIN   = 5
KEY_RIGHT_PIN  = 26
KEY_PRESS_PIN  = 13
KEY1_PIN       = 21
KEY2_PIN       = 20
KEY3_PIN       = 16

#init GPIO
GPIO.setmode(GPIO.BCM) 
GPIO.cleanup()
GPIO.setup(KEY_UP_PIN,      GPIO.IN, pull_up_down=GPIO.PUD_UP)    # Input with pull-up
GPIO.setup(KEY_DOWN_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_LEFT_PIN,    GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Input with pull-up
GPIO.setup(KEY_RIGHT_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY_PRESS_PIN,   GPIO.IN, pull_up_down=GPIO.PUD_UP) # Input with pull-up
GPIO.setup(KEY1_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY2_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up
GPIO.setup(KEY3_PIN,        GPIO.IN, pull_up_down=GPIO.PUD_UP)      # Input with pull-up

# 240x240 display with hardware SPI:
disp = LCD_1in44.LCD()
Lcd_ScanDir = LCD_1in44.SCAN_DIR_DFT  #SCAN_DIR_DFT = D2U_L2R
disp.LCD_Init(Lcd_ScanDir)
disp.LCD_Clear()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = 128
height = 128
image = Image.new('RGB', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)
disp.LCD_ShowImage(image,0,0)

# try:
while 1:
    # with canvas(device) as draw:
    if GPIO.input(KEY_UP_PIN) == 0: # button is released       
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0xff00)  #Up        
        print "Up"        
    else: # button is pressed:
        draw.polygon([(20, 20), (30, 2), (40, 20)], outline=255, fill=0)  #Up filled
        
    if GPIO.input(KEY_LEFT_PIN) == 0: # button is released
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0xff00)  #left
        print "left"        
    else: # button is pressed:       
        draw.polygon([(0, 30), (18, 21), (18, 41)], outline=255, fill=0)  #left filled
        
    if GPIO.input(KEY_RIGHT_PIN) == 0: # button is released
        draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0xff00) #right
        print "right"
    else: # button is pressed:
        draw.polygon([(60, 30), (42, 21), (42, 41)], outline=255, fill=0) #right filled       
        
    if GPIO.input(KEY_DOWN_PIN) == 0: # button is released
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0xff00) #down
        print "down"
    else: # button is pressed:
        draw.polygon([(30, 60), (40, 42), (20, 42)], outline=255, fill=0) #down filled
        
    if GPIO.input(KEY_PRESS_PIN) == 0: # button is released
        draw.rectangle((20, 22,40,40), outline=255, fill=0xff00) #center 
        print "center"
    else: # button is pressed:
        draw.rectangle((20, 22,40,40), outline=255, fill=0) #center filled
        
    if GPIO.input(KEY1_PIN) == 0: # button is released
        draw.ellipse((70,0,90,20), outline=255, fill=0xff00) #A button
        print "KEY1"
    else: # button is pressed:
        draw.ellipse((70,0,90,20), outline=255, fill=0) #A button filled
        
    if GPIO.input(KEY2_PIN) == 0: # button is released
        draw.ellipse((100,20,120,40), outline=255, fill=0xff00) #B button]
        print "KEY2"
    else: # button is pressed:
        draw.ellipse((100,20,120,40), outline=255, fill=0) #B button filled
        
    if GPIO.input(KEY3_PIN) == 0: # button is released
        draw.ellipse((70,40,90,60), outline=255, fill=0xff00) #A button
        print "KEY3"
    else: # button is pressed:
        draw.ellipse((70,40,90,60), outline=255, fill=0) #A button filled
    disp.LCD_ShowImage(image,0,0)
# except:
	# print("except")
    # GPIO.cleanup()
'''
menu.mainloop(surface)