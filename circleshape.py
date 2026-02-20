import pygame
from constants import SCREEN_WIDTH

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # must override
        pass
        
        

    def update(self, dt):
        # must override
        pass

    
    def collides_with(self,others,):
        player_pos = pygame.Vector2.move_towards(self.position)
        target_pos = pygame.Vector2.move_towards(other.position)
        if player_pos > target_pos:
            return True
        else:
            return False
        
