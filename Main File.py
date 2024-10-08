import pygame, os
from pygame import RESIZABLE

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

#Sets title bar icon to Face img
pygame.display.set_icon(faceImg)

running = True

while running:
#Lets user exit with "x"
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
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
