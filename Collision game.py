# 1. set up a background colour and draw a player character using shapes

import pygame
import random
    
class Player:
    def __init__(self):
        # setting the internal variables at start-up
        self.x = 0
        self.y = 0
        self.speed = 2.5
    def move_x(self, value):
        self.x += value
    def move_y(self, value):
        self.y += value
    def draw(self, skin = "safe"):
        x,y = self.x, self.y
        
        RED = (255, 0, 0)
        BLUE = (0, 255, 0)
        GREEN = (0, 0, 255)

        if skin == "safe" or skin == 0:
            pygame.draw.circle(screen, BLUE, [x,y], 20, 0) # draw a circle - centre x, centre y, radius, line width
            pygame.draw.rect(screen, GREEN, pygame.Rect(x-20,y-20, 40, 10)) # draw a rectangle - screen, colour, ( top left x coord, top left y coord, width, height )
            pygame.draw.polygon(screen, RED, points=[(x-15,y-21), (x,y-40), (x+15,y-21)]) # draw a polygon - 1st coord, 2nd coord, 3rd coord
            #pygame.draw.line(screen, RED, (x,y), (x+120, y+60), 20) # draw a line - screen, colour, 1st coord, 2nd coord, width in pixels
            #pygame.draw.ellipse(screen, RED, (x, y, 200, 100), 0) #draw an ellipse - screen, colour, ( top left x coord, top left y coord , width, height), fill
            pygame.draw.polygon(screen, RED, points=[(x+10,y-40), (x+20,y-52), (x+56,y-22), (x+46,y-10)])
        elif skin == "crashed" or skin == 1:
            pygame.draw.circle(screen, RED, [x,y], 30, 5) # draw a circle - centre x, centre y, radius, line width

class Enemy:
    def __init__(self):
        self.x = random.randint(-screen_size, screen_size)
        self.y = random.randint(-screen_size, screen_size)
        self.speed = 1
    def move_x(self, value):
        self.x += value
    def move_y(self, value):
        self.y += value
    def draw(self):
        x,y = self.x, self.y
    
        RED = (255, 0, 0) # set up your own colours
        BLUE = (0, 255, 0)
        GREEN = (0, 0, 255)

        pygame.draw.circle(screen, RED, [x,y], 30, 5) # draw a circle - centre x, centre y, radius, line width
        
########################################################
# main code
pygame.init()

clock = pygame.time.Clock()

# set the screen dimensions
screen_size = 750
screen = pygame.display.set_mode([screen_size, screen_size])
player = Player()
enemy = Enemy()
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # listen for keypress
    if keys[pygame.K_UP]:
        player.move_y(-player.speed)
    if keys[pygame.K_DOWN]:
        player.move_y(player.speed)
    if keys[pygame.K_LEFT]:
        player.move_x(-player.speed)
    if keys[pygame.K_RIGHT]:
        player.move_x(player.speed)
    # draw to the screen
    safeColour = (47, 181, 65) # add the safe background colour 
    screen.fill(safeColour)
    player.draw()
    enemy.draw()
    
    # Flip the display
    pygame.display.flip()
    clock.tick(60)
# Done! Time to quit.
pygame.quit()
