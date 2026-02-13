from logger import log_state
import pygame
from constants import SCREEN_WIDTH
from constants import SCREEN_HEIGHT
def main():
        print("Starting Asteroids with pygame version: 2.6.1")
        print("Screen width: 1280 Screen height: 720")
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        while True:
                log_state()
                for event in pygame.event.get():
                        pass
        
                screen.fill("black")
                pygame.display.flip()

if __name__ == "__main__":
    main()
    
