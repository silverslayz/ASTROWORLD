from logger import log_state
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event

def main():
    pygame.init()
    

    # 1. Create all groups FIRST
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # 2. Set containers AFTER groups exist
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)

    # 3. Create instances AFTER containers are set
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player(x, y)
    AsteroidField()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # ... rest of game loop stays the same


    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)
        for obj in asteroids:
            if

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
