# 1. set up a background colour and draw a player character using shapes

import pygame

def getPos():
    pos = pygame.mouse.get_pos()
    return (pos)

def drawObstacle():
    pass

def drawCharacter():
    x,y = getPos() # get the x,y position of the mouse
    
    RED = (255, 0, 0) # set up your own colours
    BLUE = (0, 255, 0)
    GREEN = (0, 0, 255)

    pygame.draw.circle(screen, BLUE, [x,y], 20, 0) # draw a circle - centre x, centre y, radius, line width
    pygame.draw.rect(screen, GREEN, pygame.Rect(x-20,y-20, 40, 10)) # draw a rectangle - screen, colour, ( top left x coord, top left y coord, width, height )
    pygame.draw.polygon(screen, RED, points=[(x-15,y-21), (x,y-40), (x+15,y-21)]) # draw a polygon - 1st coord, 2nd coord, 3rd coord
    #pygame.draw.line(screen, RED, (x,y), (x+120, y+60), 20) # draw a line - screen, colour, 1st coord, 2nd coord, width in pixels
    #pygame.draw.ellipse(screen, RED, (x, y, 200, 100), 0) #draw an ellipse - screen, colour, ( top left x coord, top left y coord , width, height), fill
    pygame.draw.polygon(screen, RED, points=[(x+10,y-40), (x+20,y-52), (x+56,y-22), (x+46,y-10)])
def draw():    
    safeColour = (47, 181, 65) # add the safe background colour 
    screen.fill(safeColour)
    drawObstacle() # draw obstacles
    drawCharacter() # draw character
    

########################################################
# main code
pygame.init()

# set the screen dimensions
screen = pygame.display.set_mode([500, 500])

# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw to the screen
    draw()
    
    # Flip the display
    pygame.display.flip()
    
# Done! Time to quit.
pygame.quit()
