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

#Loads the image of the face
faceImg = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images','William_img.jpg')).convert_alpha()

#Load second image, transform to the right size
faceImg2 = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images','IMG_E0994.JPG')).convert_alpha()
faceImg2 = pygame.transform.scale(faceImg2, (281,360))

#Sets title bar icon to Face img
pygame.display.set_icon(faceImg)

#Variables used for changing face img when lmb is pressed
buttonDown = 0
timeVar = 0

running = True

while running:
    for event in pygame.event.get():
#Lets user exit with "x"
        if event.type == pygame.QUIT:
            running = False
#Changes face img when lmb is pressed
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            faceImg = faceImg2
            buttonDown = 1
#Changes face img back after 1/2 sec
    if buttonDown == 1:
            timeVar +=1
            if timeVar == 30:
                faceImg = pygame.image.load(os.path.join(os.path.dirname(__file__), 'Images','William_img.jpg')).convert_alpha()
                timeVar = 0
                buttonDown = 0
#Sets background color to cyan
    screen.fill(color=(0, 250, 250))
#This bit of code centers the Face img on the mouse
    pos = pygame.mouse.get_pos()
    facePos = list(pos)
    facePos[0] -= 141
    facePos[1] -= 180
    facePos = tuple(facePos)
#Blits the Face img to screen
    screen.blit(faceImg, facePos)
    pygame.display.flip()
    clock.tick(60)
