# 1. set up a background colour and draw a player character using shapes

import pygame
import random
    
class Player:
    def __init__(self):
        # setting the internal variables at start-up
        self.x = screen_size/2
        self.y = screen_size/2
        # center the player in the middle of the screen
        self.rect = pygame.Rect(self.x-50, self.y-50, 100, 100)
        self.speed = 4
    def move_x(self, value):
        self.x += value
    def move_y(self, value):
        self.y += value
    def draw(self, skin = "safe"): # safe by default
        x,y = self.x, self.y
        rects = []
        
        RED = (200, 72, 72)
        BLUE = (24, 72, 88)
        GOLD = (248, 200, 40)
        
        if skin == "safe" or skin == 0:
##            pygame.draw.circle(screen, BLUE, [x,y], 20, 0) # draw a circle - centre x, centre y, radius, line wid
##            pygame.draw.rect(screen, GOLD, pygame.Rect(x-20,y-20, 40, 10)) # draw a rectangle - screen, colour, ( top left x coord, top left y coord, width, height )
##            pygame.draw.polygon(screen, RED, points=[(x-15,y-21), (x,y-40), (x+15,y-21)]) # draw a polygon - 1st coord, 2nd coord, 3rd coord
##            #pygame.draw.line(screen, RED, (x,y), (x+120, y+60), 20) # draw a line - screen, colour, 1st coord, 2nd coord, width in pixels
##            #pygame.draw.ellipse(screen, RED, (x, y, 200, 100), 0) #draw an ellipse - screen, colour, ( top left x coord, top left y coord , width, height), fill
##            pygame.draw.polygon(screen, RED, points=[(x+10,y-40), (x+20,y-52), (x+56,y-22), (x+46,y-10)])
##            self.rect = pygame.Rect(x-50, y-50, 100, 100)

            
            rects.append(pygame.draw.rect(screen, GOLD, pygame.Rect(x-20, y-15, 40, 20)))
            rects.append(pygame.draw.rect(screen, BLUE, pygame.Rect(x-30, y-30, 20, 35)))
            rects.append(pygame.draw.rect(screen, RED, pygame.Rect(x-35, y-35, 30, 5)))
            rects.append(pygame.draw.polygon(screen, GOLD, [(x+20, y-15), (x+20, y+5), (x+40, y+5)]))
            rects.append(pygame.draw.circle(screen, RED, [x-25, y+10], 10))
            rects.append(pygame.draw.circle(screen, RED, [x+5, y+10], 5))
            rects.append(pygame.draw.circle(screen, RED, [x+20, y+10], 5))


            
            self.rect = self.rect.unionall(rects)

            print(rects)
        elif skin == "crashed" or skin == 1:
            pygame.draw.circle(screen, (255, 0, 0), [x,y], 30, 5) # draw a circle - centre x, centre y, radius, line width

class Enemy:
    def __init__(self):
        self.x = random.randint(-screen_size, screen_size)
        self.y = 0#random.randint(-screen_size, screen_size)
        self.rect = self.rect = pygame.Rect(self.x-50, self.y-50, 100, 100)
        self.speed = 1
    def move_x(self, value):
        self.x += value
    def move_y(self, value):
        
        self.y += value
    def draw(self):
        x,y = self.x, self.y
    
        RED = (255, 0, 0) # set up your own colours
        BLUE = (0, 255, 0)
        GOLD = (0, 0, 255)

        pygame.draw.circle(screen, RED, [x,y], 30, 5) # draw a circle - centre x, centre y, radius, line width
        self.rect = pygame.Rect(x-50, y-50, 100, 100)

class Point:
    def __init__(self):
        self.x = random.randint(-screen_size, screen_size)
        self.y = screen_size#random.randint(-screen_size, screen_size)
        self.rect = pygame.Rect(self.x-50, self.y-50, 100, 100)
    def draw(self):
        x,y = self.x, self.y
    
        RED = (255, 0, 0) # set up your own colours
        BLUE = (0, 255, 0)
        GOLD = (0, 0, 255)

        pygame.draw.circle(screen, BLUE, [x,y], 30, 5) # draw a circle - centre x, centre y, radius, line width
        self.rect = pygame.Rect(x-50, y-50, 100, 100)
    def move_y(self, value):
        
        self.y += value
        
########################################################
# main code
pygame.init()

clock = pygame.time.Clock()

# set the screen dimensions
screen_size = 750
screen = pygame.display.set_mode([screen_size, screen_size])
player = Player()
enemies = []
points = []
count = 0
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # listen for keypress
##    if keys[pygame.K_UP]:
##        player.move_y(-player.speed)
##    if keys[pygame.K_DOWN]:
##        player.move_y(player.speed)
##    if keys[pygame.K_LEFT]:
##        player.move_x(-player.speed)
##    if keys[pygame.K_RIGHT]:
##        player.move_x(player.speed)
    if keys[pygame.K_SPACE]:
        player.move_x(player.speed)
    else:
        player.move_x(-player.speed)
    
    count += 1
    if count % 30 == 0:
        points.append(Point())
        enemies.append(Enemy())

    
    # draw to the screen
    safeColour = (47, 181, 65) # add the safe background colour 
    screen.fill(safeColour)
    player.draw()
    for enemy in enemies:
        enemy.draw()
        enemy.move_y(5)
        if pygame.Rect.colliderect(player.rect, enemy.rect):
            print("Hit!")
            enemies.remove(enemy)
    for point in points:
        point.draw()
        point.move_y(-5)
        if pygame.Rect.colliderect(player.rect, point.rect):
            print("Point!")
            points.remove(point)
    
    # Flip the display
    pygame.display.flip()
    clock.tick(60)
# Done! Time to quit.
pygame.quit()
