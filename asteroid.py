from CircleShape import CircleShape
from constants import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (0, 255, 0), self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)