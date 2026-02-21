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

# screen variables 
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2


    # 4. Add a helper to reset a run
    def reset_game():
        updatable.empty()
        drawable.empty()
        asteroids.empty()
        shots.empty()

        player = Player(x, y)
        AsteroidField()
        return player, 0, 3

   
    

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()


    font = pygame.font.Font(None, 64)
    state = "menu"
    player = None
    score = 0
    lives = 3



    # ... rest of game loop stays the same


    while True:
        hit = False
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                if state in ("menu", "game_over"):
                    player, score, lives = reset_game()
                    state = "playing"
                        

        dt = clock.tick(60) / 1000
        if state == "menu":
            screen.fill("black")
            text = font.render("Press Enter to Start", True, "white")
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)))
            pygame.display.flip()
            continue
        if state == "game_over":
            screen.fill("black")
            text = font.render(f"Game Over  Score: {score}", True, "white")
            sub = pygame.font.Font(None, 48).render("Press Enter for Menu", True, "white")
            screen.blit(text, text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 40)))
            screen.blit(sub, sub.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 20)))
            pygame.display.flip()
            continue


        if state != "playing":
            continue

        updatable.update(dt)
        
        for obj in asteroids:
            if obj.collides_with(player):
                log_event("player_hit")
                lives -= 1
                hit = True
                break


        if lives <= 0:
            state = "game_over"
            updatable.empty(); drawable.empty(); asteroids.empty(); shots.empty()
            continue
        
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
