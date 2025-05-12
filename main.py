import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    while True:
        # Check for events (like window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black
        screen.fill("black")
        
        # Update the display
        pygame.display.flip()



if __name__ == "__main__":
    main()