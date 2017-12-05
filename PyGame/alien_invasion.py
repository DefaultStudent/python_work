import sys
import pygame

def run_game():
    # init the game and create a screen object
    pygame.init()
    screen = pygame.display.set_mode((1200, 800))
    pygame.display.set_caption("Alien Invasion")

    # set the background color
    bg_color = (230, 230, 230)

    # the main loop of start game
    while True:

        # the monitor of keyboard and mouse
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        #redisplay the screen everytime when the loop
        screen.fill(bg_color)

        # show the screen
        pygame.display.flip()

run_game()