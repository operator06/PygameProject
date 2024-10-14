import pygame, sys, os
from pygame import *

#Create method called main_menu that takes screen and windowListUnch as parameters
def main_menu(screen,windowListUnch,catImg1):
    running = True

    pygame.display.set_icon(catImg1)

# Load background music
    pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Sounds and Music', 'Main Menu Music.mp3'))
# Plays background music
    pygame.mixer.music.play()

#Create font for the menu title
    font1 = pygame.font.Font(None, 250)
#Create font for the buttons
    font2 = pygame.font.Font(None, 90)

#Render menu title font and have it say Bad Cat!
    menuSurf = font1.render("Bad Cat!", False, (255, 255, 255))
#Render the button word as Play
    buttonFont = font2.render("Play", False, (0,0,0))
#Render the quit button word as Quit
    quitFont = font2.render("Quit", False, (0,0,0))

#Get the right x and y coordinates for the menu title
    windowListChng = windowListUnch
    windowListChng[0] -= 1100
    windowListChng[1] -= 750

#Make a Rect for the button
    buttonRect = pygame.Rect(windowListChng[0]+200,windowListChng[1]+500, 300, 100)
#Make a surface for the button
    buttonSurf = pygame.Surface((buttonRect.w,buttonRect.h))
#Color the button surface white
    buttonSurf.fill(color=(255,255,255))

#Make a Rect for the start button outline
    butOutRect = pygame.Rect(windowListChng[0]+195,windowListChng[1]+495, 310, 110)
#Make a surface for the start button outline
    butOutSurf = pygame.Surface((butOutRect.w,butOutRect.h))
#Color the outline surface black
    butOutSurf.fill(color=(0,0,0))

# Make a Rect for the quit button
    quitRect = pygame.Rect(windowListChng[0] + 200, windowListChng[1] + 630, 300, 100)
# Make a surface for the quit button
    quitSurf = pygame.Surface((quitRect.w, quitRect.h))
# Color the quit button surface white
    quitSurf.fill(color=(255, 255, 255))

# Make a Rect for the quit button outline
    quitOutRect = pygame.Rect(windowListChng[0] + 195, windowListChng[1] + 625, 310, 110)
# Make a surface for the quit button outline
    quitOutSurf = pygame.Surface((quitOutRect.w, quitOutRect.h))
# Color the outline surface black
    quitOutSurf.fill(color=(0, 0, 0))

#Main loop
    while running:
        mousePos = pygame.mouse.get_pos()
#Ends game if user presses x
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
#Exits main menu into game when button is pressed
            if event.type == MOUSEBUTTONDOWN and event.button == 1:
                if buttonRect.collidepoint(mousePos):
                    running = False
                if quitRect.collidepoint(mousePos):
                    pygame.quit()
                    sys.exit()
#Set background screen to cyan
        screen.fill(color=(0, 255, 255))
#Blit menu title to screen at right position
        screen.blit(menuSurf, (windowListChng[0],windowListChng[1]))
        if buttonRect.collidepoint(mousePos):
            screen.blit(butOutSurf, (butOutRect.x, butOutRect.y))
        if quitRect.collidepoint(mousePos):
            screen.blit(quitOutSurf, (quitOutRect.x, quitOutRect.y))
#Blit button and its text to screen at right position
        screen.blit(buttonSurf, (buttonRect.x,buttonRect.y))
        screen.blit(buttonFont, (buttonRect.x+85,buttonRect.y+20))
#Blit quit button and its text to screen at right position
        screen.blit(quitSurf, (quitRect.x,quitRect.y))
        screen.blit(quitFont, (quitRect.x+85,quitRect.y+20))
#Update the display
        pygame.display.flip()