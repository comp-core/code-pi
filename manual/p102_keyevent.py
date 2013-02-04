# Example from Pi Educational Manual v1.0 P. 102
# Provided under a Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License

def keyEvent(self, event): 
    # event should be key event but we only move 
    # if the key is pressed down and not released up
    self.keydir = (0 if event.type == pygame.KEYUP else
-1 if event.key == pygame.K_LEFT else
+1 if event.key == pygame.K_RIGHT else 0)

# pygame library wants to do a few things before we can use it
pygame.init()
pygame.display.set_caption("Ski Slalom")
pygame.key.set_repeat(100, 5)

# create something to draw on with a size of 400 wide
canvas = pygame.display.set_mode([400, 500])

# we will need to have a constant time between frames
clock = pygame.time.Clock()
world = skiWorld()

# check input, change the game world and display the new game world
while (world.running):
    
    # check external events (key presses, for instance)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # stop running the game
            world.running = False
        elif (hasattr(event, 'key')): # process this keyboard input
            world.keyEvent(event)
    # update the game world
    world.updateWorld()
    
    # draw the world on the canvas
    world.drawWorld(canvas)
    
    # important to have a constant time between each display flip.
    # in this case, wait until at least 1/30th second has passed
    clock.tick(30)
    # flip the display to show the newly drawn screen
    pygame.display.flip()

# once the game is not running, need to finish up neatly
pygame.quit()
