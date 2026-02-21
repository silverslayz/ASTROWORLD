from logger import log_state
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT,Point
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event,log_state
import sys
from shot import Shot
def main():
    pygame.init()
    

    # 1. Create all groups FIRST
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # 2. Set containers AFTER groups exist
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (drawable,updatable,shots)

    # 3. Create instances AFTER containers are set
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    AsteroidField()
    score = 0
    lives = 3
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    # ... rest of game loop stays the same


    while lives > 0:
        hit = False
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        dt = clock.tick(60) / 1000

        updatable.update(dt)
        
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                lives -= 1
                hit = True
                break
        if lives <= 0:
            print("Game over")
            print(f"Your high score was {score}")
            sys.exit()
        if hit:
            player.kill()
            player = Player(x,y)
            continue

        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        for asteroid in list(asteroids):
            for shot in list(shots):
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()
                    log_event("point increase")
                    score += 1
        
       
        
        
                    
                


if __name__ == "__main__":
    main()
