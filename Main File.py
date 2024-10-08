import pygame, os

pygame.init()

#Get the size of desktop
windowSize = pygame.display.get_desktop_sizes()
#Convert that size to a list
windowList = list(windowSize[0])
#save windowList before it's changed
windowListUnch = windowList
#Lower the y by 30
windowList[1] -= 30
#Convert back to tuple
windowSize = tuple(windowList)

#This bit of code sets the top of the title bar to the top of the screen
x = 0
y = 30
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)

screen = pygame.display.set_mode(windowSize)


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
