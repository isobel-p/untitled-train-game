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
        self.lives = 3
    def move(self, value):
        self.x += value
    #def move(self, value):
    #    self.y += value
    def draw(self, skin = "safe"): # safe by default
        x,y = self.x, self.y
        rects = []
        self.rect = pygame.Rect(self.x,self.y,0,0)
        RED = (200, 72, 72)
        BLUE = (24, 72, 88)
        GOLD = (248, 200, 40)
        # shows different skins depending on player position      
        if skin == "safe" or skin == 0:
            # pygame.draw function returns a Rect object -
            # each Rect is added to the list of rectangles
            rects.append(pygame.draw.rect(screen, GOLD, pygame.Rect(x-20, y-15, 40, 20)))
            rects.append(pygame.draw.rect(screen, BLUE, pygame.Rect(x-30, y-30, 20, 35)))
            rects.append(pygame.draw.rect(screen, RED, pygame.Rect(x-35, y-35, 30, 5)))
            rects.append(pygame.draw.polygon(screen, GOLD, [(x+20, y-15), (x+20, y+5), (x+40, y+5)]))
            rects.append(pygame.draw.circle(screen, RED, [x-25, y+10], 10))
            rects.append(pygame.draw.circle(screen, RED, [x+5, y+10], 5)) 
            rects.append(pygame.draw.circle(screen, RED, [x+20, y+10], 5))
        elif skin == "crashed" or skin == 1:
            rects.append(pygame.draw.rect(screen, RED, pygame.Rect(x-20, y-15, 40, 20)))
            rects.append(pygame.draw.rect(screen, RED, pygame.Rect(x-30, y-30, 20, 35)))
            rects.append(pygame.draw.rect(screen, RED, pygame.Rect(x-35, y-35, 30, 5)))
            rects.append(pygame.draw.polygon(screen, RED, [(x+20, y-15), (x+20, y+5), (x+40, y+5)]))
            rects.append(pygame.draw.circle(screen, RED, [x-25, y+10], 10))
            rects.append(pygame.draw.circle(screen, RED, [x+5, y+10], 5)) 
            rects.append(pygame.draw.circle(screen, RED, [x+20, y+10], 5))
        elif skin == "point" or skin == 2:
            rects.append(pygame.draw.rect(screen, GOLD, pygame.Rect(x-20, y-15, 40, 20)))
            rects.append(pygame.draw.rect(screen, GOLD, pygame.Rect(x-30, y-30, 20, 35)))
            rects.append(pygame.draw.rect(screen, GOLD, pygame.Rect(x-35, y-35, 30, 5)))
            rects.append(pygame.draw.polygon(screen, GOLD, [(x+20, y-15), (x+20, y+5), (x+40, y+5)]))
            rects.append(pygame.draw.circle(screen, GOLD, [x-25, y+10], 10))
            rects.append(pygame.draw.circle(screen, GOLD, [x+5, y+10], 5)) 
            rects.append(pygame.draw.circle(screen, GOLD, [x+20, y+10], 5))
        self.rect = self.rect.unionall(rects) # combines all the Rect objects into one hitbox rectangle
        # pygame.draw.rect(screen, (random.randint(0,255),random.randint(0,255),random.randint(0,255)), self.rect) # rainbow hitbox!

        
class Enemy:
    def __init__(self):
        self.x = random.randint(-screen_size, screen_size) # Places the enemy randomly along the top of the screen
        self.y = 0#random.randint(-screen_size, screen_size)
        self.rect = self.rect = pygame.Rect(self.x-50, self.y-50, 100, 100)
        self.speed = 1
        self.surf = pygame.image.load("enemy.png").convert_alpha()
        self.rect = self.surf.get_rect(center=(self.x, 0))
    def move(self, value):
        self.y += value
    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        self.rect = self.surf.get_rect(center=(self.x, self.y))

        
class Point:
    def __init__(self):
        self.x = random.randint(-screen_size, screen_size)
        self.y = screen_size#random.randint(-screen_size, screen_size)
        self.rect = pygame.Rect(self.x-50, self.y-50, 100, 100)
        self.surf = pygame.image.load("point.png")
        self.rect = self.surf.get_rect(center=(self.x, screen_size))
    def draw(self):
        screen.blit(self.surf, (self.x, self.y))
        self.rect = self.surf.get_rect(center=(self.x, self.y))
    def move(self, value):
        self.y += value


class BgObject:
    def __init__(self):
        self.x = 0
        self.y = random.randint(0, screen_size)
        self.speed = abs(screen_size/2-self.y)/10
    def draw(self):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(self.x-10, self.y-10, 20, 20))
        self.x += self.speed
        
########################################################
# main code
pygame.init()  

clock = pygame.time.Clock()

# set the screen dimensions
screen_size = 800#int(input("Enter screen size: "))
screen = pygame.display.set_mode([screen_size, screen_size])
player = Player()
enemies = []
points = []
count = 0
bg = pygame.image.load("grass.png")
bg_objects = []
hit = 0
# Run until the user asks to quit
running = True
while running:
    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed() # listen for keypress

    if keys[pygame.K_SPACE]:
        player.move(player.speed)
    else:
        player.move(-player.speed)
    
    count += 1
    if count % 30 == 0:
        points.append(Point())
        
        bg_objects.append(BgObject())
    if count % 10 == 0:
        enemies.append(Enemy())
    if player.x < 0:
        #print("Out of bounds")
        player.lives -= 1
        player.move(screen_size/2)
        print(player.lives)
    if player.x > screen_size:
        #print("Out of bounds")
        player.lives -= 1
        player.move(-screen_size/2)
    # draw to the screen
##    safeColour = (47, 181, 65) # add the safe background colour 
##    screen.fill(safeColour)
    screen.blit(bg, (0,0))
    for enemy in enemies:
        enemy.draw()
        enemy.move(5)
        # deletes the enemy/point once it goes out of bounds
        if enemy.y > screen_size:
            enemies.remove(enemy)
        if pygame.Rect.colliderect(player.rect, enemy.rect):
            #print("Hit!")
            enemies.remove(enemy)
            player.lives -= 1
            hit = 15
    for point in points:
        point.draw()
        point.move(-5)
        # deletes the enemy/point once it goes out of bounds
        if point.y < 0:
            points.remove(point)
        if pygame.Rect.colliderect(player.rect, point.rect):
            #print("Point!")
            points.remove(point)
            player.lives += 1
            hit = -15
    for bg_object in bg_objects:
        bg_object.draw()
        # deletes the enemy/point once it goes out of bounds
        if bg_object.x > screen_size:
            bg_objects.remove(bg_object)
        
    if hit > 0:
        player.draw(1)
        hit -= 1
    elif hit < 0:
        player.draw(2)
        hit += 1
    else:
        player.draw()
    a=20
    for i in range(player.lives):
        pygame.draw.rect(screen, (0,0,0), pygame.Rect(a, screen_size-70, 50, 50))
        a+=70
    if player.lives <= 0:
        running = False
    # Flip the display
    pygame.display.flip()
    clock.tick(60)
# Done! Time to quit.
pygame.quit()
