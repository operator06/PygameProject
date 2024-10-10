import pygame, os
from pygame import RESIZABLE, MOUSEBUTTONDOWN
from random import randint

pygame.init()

#Changes title to "Project Prototype"
pygame.display.set_caption('Project Prototype')

clock = pygame.time.Clock()

#This bit of code figures how big the window needs to be depending on user's screen size
windowSize = pygame.display.get_desktop_sizes()
windowList = list(windowSize[0])
windowListUnch = windowList
windowList[1] -= 30
windowSize = tuple(windowList)

#This bit of code sets the top of the title bar to the top of the screen
x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

#Create the display. Make it right size and let user change size
screen = pygame.display.set_mode(windowSize, flags=RESIZABLE)

#Makes the mouse invisible
pygame.mouse.set_visible(False)

#Loads the image of the spray bottle
sprayBtImg1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Spray Bottle 1.jpg')).convert_alpha()

#Load second image
sprayBtImg2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Spray Bottle 2.jpg')).convert_alpha()

#This code gets the mouse position so the spray Rect can be on it
pos = pygame.mouse.get_pos()
sprayPos = list(pos)
sprayPos[0] -= 141
sprayPos[1] -= 180

#Create Rect for the spray bottle img and position it on the mouse
sprayRect = pygame.Rect(sprayPos[0],sprayPos[1],204,358)

#Load the spray sound effect
spraySound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds and Music', 'Spray Bottle sfx.wav'))

#Load cat image 1
catImg1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Cat Image1.jpg')).convert_alpha()

#Load cat image 2
catImg2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Cat Image2.jpg')).convert_alpha()

#Create random numbers for the cat's x and y coordinate
rand1 = randint(0,windowListUnch[0] - 204)
rand2 = randint(0,windowListUnch[1] - 358)

#Create a Rect for the cat img and place it at rand1 and rand2's position
catRect = pygame.Rect(rand1,rand2,204,358)

#Load the cat's meow sfx
catSound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds and Music', 'Cat Meow.wav'))

#Load background music
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Sounds and Music','Jazz Music.mp3'))
#Plays background music
pygame.mixer.music.play()

#Sets title bar icon to spray bottle img
pygame.display.set_icon(sprayBtImg1)

#Variables used for changing spray bottle img when lmb is pressed
buttonDown = 0
timeVar = 0
#Variable for changing cat img back after lmb is pressed
timeVar1 = 0

running = True

#This is the main game loop
while running:
    for event in pygame.event.get():
#Lets user exit with "x"
        if event.type == pygame.QUIT:
            running = False
#Changes spray bottle img and cat img when lmb is pressed
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            sprayBtImg1 = sprayBtImg2
#Changes cat Img if catRect and sprayRect collide
            if sprayRect.colliderect(catRect):
                catImg1 = catImg2
                catSound.play()
            buttonDown = 1
#Play spray sound effect when lmb is pressed
            spraySound.play()
#Changes spray bottle img back after 1/2 sec
    if buttonDown == 1:
            timeVar +=1
            if timeVar == 30:
                sprayBtImg1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Spray Bottle 1.jpg')).convert_alpha()
                timeVar = 0
                buttonDown = 0
#Changes cat img back and sets its new random position after a 1/2 sec
    if catImg1 == catImg2:
        timeVar1 += 1
        if timeVar1 == 30:
            catImg1 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images', 'Cat Image1.jpg')).convert_alpha()
            rand1 = randint(0, windowListUnch[0] - 204)
            rand2 = randint(0, windowListUnch[1] - 358)
            catRect = pygame.Rect(rand1, rand2, 204, 358)
            timeVar1 = 0
#Sets background color to green
    screen.fill(color=(0, 250, 0))
#This bit of code centers the spray bottle Rect on the mouse
    pos = pygame.mouse.get_pos()
    sprayPos = list(pos)
    sprayPos[0] -= 141
    sprayPos[1] -= 180
    sprayRect = pygame.Rect(sprayPos[0],sprayPos[1],204,358)
#Blits the cat img to screen at catRect position
    screen.blit(catImg1, catRect)
#Blits the spray bottle img to screen at sprayRect position
    screen.blit(sprayBtImg1, sprayRect)
    pygame.display.flip()
    clock.tick(60)
