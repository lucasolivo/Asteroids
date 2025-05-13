import pygame
from constants import *
from player import *
from asteroid import *
from asteroidField import *
from shot import *

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField()
    P1 = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    
    
    
    while True:
        # Check for events (like window close)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        # Fill the screen with black
        screen.fill("black")
        for obj in updatable:
            obj.update(dt)
        for obj in drawable:
            obj.draw(screen)

        for obj in asteroids:
            if obj.collision(P1):
                print("Game Over!")
                return
        for obj in asteroids:
            for bul in shots:
                if obj.collision(bul):
                    obj.split()
                    bul.kill()

        
        
        # Update the display
        pygame.display.flip()
        
        dt = clock.tick(60)/1000



if __name__ == "__main__":
    main()