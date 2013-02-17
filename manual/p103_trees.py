# Example from Pi Educational Manual v1.0 P. 102
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

import random
class worldTreeGroup(pygame.sprite.Group):
    speed = 5

    def __init__(self, picture):
        pygame.sprite.Group.__init__(self)
        treePicture = picture
        treeRow = pygame.sprite.Group()
        
        # in rows with a gap somewhere in the middle
        # only have a line of trees every 5th row or the
        # game is too difficult
        for y in range(0, 400):
            if (y % 5 == 0): # every 5th, add tree row with a gap
                gapsize = 3 + random.randint(0,6) # size of gap
                # starting position of gap
                gapstart = random.randint(0,10 - (gapsize//2))
                
                # create a row of 20 trees but 'gapsize'
                # skip trees in the middle
                for b in range(0,20):
                    if b >= gapstart and gapsize > 0:
                        gapsize-=1
                    else:
                        newtree=worldSprite([b*20, (y+10)*20], treePicture)
                        treeRow.add(newtree)
            
            self.add(treeRow)
    def update(self):
        for treeRow in self:
            treeRow.rect.top-=self.speed
            if treeRow.rect.top <= -20:
                treeRow.kill() # remove this block from ALL groups
