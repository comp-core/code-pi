# Example from Pi Educational Manual v1.0 P. 100
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

# pyGameSkier.py
import pygame
# a world sprite is a pygame sprite
class worldSprite(pygame.sprite.Sprite):
    def __init__(self, location, picture):
        pygame.sprite.Sprite.__init__(self)
        self.image = picture
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
    def draw(self,screen):
        screen.blit(self.image, self.rect)
            # draw this sprite on the screen (BLIT)

# a skier in the world knows how fast it is going
# and it can move horizontally
class worldSkier(worldSprite):
    speed = 5
    def update(self, direction):
        self.rect.left += direction * self.speed
        self.rect.left = max(0, min(380, self.rect.left))

class skiWorld(object):
    running = False
    keydir = 0
    
    def __init__(self):
        self.running = True
        self.skier = worldSkier([190, 50], pygame.image.load("skier.png"))
    def updateWorld(self):
        # the skier is part of the world and needs updating
        self.skier.update(self.keydir)
    def drawWorld(self, canvas):
        canvas.fill([255, 250, 250])  # make a snowy white background
        world.skier.draw(canvas) # draw the player on the screen
