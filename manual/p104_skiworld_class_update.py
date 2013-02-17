# Example from Pi Educational Manual v1.0 P. 104
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License


def __init__(self):
    self.running = True
    self.skier = worldSkier([190, 50], pygame.image.load("skier.png"))
    
## adding trees
    self.trees = worldTreeGroup(pygame.image.load("block.png"))
    def updateWorld(self):
        # the skier is part of the world and needs updating
        self.skier.update(self.keydir)
        ## move the tree rows - removing any
        ## line that is off the top of the screen
        self.trees.update()
        ## check if the skier has collided with any 
        ## tree sprite in the tree rows in the tree group
        if pygame.sprite.spritecollide(self.skier, self.trees, False):
            self.running = False
        ## check if the tree group has run out of tree rows – 
        ## skier got to the bottom of the piste
        if len(self.trees)==0:
            self.running = False
    def drawWorld(self, canvas):
        canvas.fill([255, 250, 250]) # make a snowy white background
        world.trees.draw(canvas) # draw the trees
        world.skier.draw(canvas) # draw the player on the screen
