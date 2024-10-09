import pygame, os
from pygame import RESIZABLE, MOUSEBUTTONDOWN

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

#Load the spray sound effect
spraySound = pygame.mixer.Sound(os.path.join(os.path.dirname(__file__), 'Sounds and Music', 'Spray Bottle sfx.wav'))

#Load background music
pygame.mixer.music.load(os.path.join(os.path.dirname(__file__), 'Sounds and Music','Jazz Music.mp3'))
#Plays background music
pygame.mixer.music.play()

#Sets title bar icon to spray bottle img
pygame.display.set_icon(sprayBtImg1)

#Variables used for changing spray bottle img when lmb is pressed
buttonDown = 0
timeVar = 0

running = True

while running:
    for event in pygame.event.get():
#Lets user exit with "x"
        if event.type == pygame.QUIT:
            running = False
#Changes spray bottle img when lmb is pressed
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            sprayBtImg1 = sprayBtImg2
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
#Sets background color to green
    screen.fill(color=(0, 250, 0))
#This bit of code centers the spray bottle img on the mouse
    pos = pygame.mouse.get_pos()
    facePos = list(pos)
    facePos[0] -= 141
    facePos[1] -= 180
    facePos = tuple(facePos)
#Blits the spray bottle img to screen
    screen.blit(sprayBtImg1, facePos)
    pygame.display.flip()
    clock.tick(60)
