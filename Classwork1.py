import pygame
# initialise pygame
pygame.init()


# seting a with of 500 and height of 600
window = pygame.display.set_mode((500,600))

#

# displaying a window of height 500 and width 400
window = pygame.display.set_mode((500, 800))

red = (255,0,0)
# Here we set name or title of our pygame window
pygame.display.set_caption('precious')
yellow = (255,255,0)
blue = (0, 0, 255)
green = (0, 255,0 )
black = (0, 0, 0)
white = (255,255,255)

pygame.draw.rect(window, yellow, pygame.Rect(0, 0, 65, 60))
pygame.draw.rect(window, yellow, pygame.Rect(20, 10, 26, 30))
pygame.draw.rect(window, yellow, pygame.Rect(40, 10, 25, 30))
pygame.draw.rect(window, yellow, pygame.Rect(5, -10, 32, 30))

#creating a bool which checks if game is running
running = True
# keep game running till running is true
while running:

    # Check for event user pushed event in queue
    for event in pygame.event.get():
        # if event is of type then
        # set running bool false
        if event.type==pygame.QUIT:
            running = False