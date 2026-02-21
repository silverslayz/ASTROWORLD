import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS, SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_event
import random
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)
        
       
    def update(self,dt):
        self.position += self.velocity * dt

        r = self.radius
        if self.position.x < -r:
            self.position.x = SCREEN_WIDTH + r
        elif self.position.x > SCREEN_WIDTH + r:
            self.position.x = -r

        if self.position.y < -r:
            self.position.y = SCREEN_HEIGHT + r
        elif self.position.y > SCREEN_HEIGHT + r:
            self.position.y = -r

    def draw(self,screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            random_angle = random.uniform(20,50)
            vel = self.velocity
            vel1 =  vel.rotate(random_angle)
            vel2 = vel.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1= Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid2 = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteroid1.velocity = vel1 * 1.2
            new_asteroid2.velocity = vel2 * 1.2