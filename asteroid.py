import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event
import random
from player import Player
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen) -> None:
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    def update(self, dt: float,) -> None:
        self.position += self.velocity * dt
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        velocity_1 = self.velocity.rotate(random.uniform(20, 50))
        velocity_2 = self.velocity.rotate(random.uniform(-50, -20))
        self.asteroid_new_radius = self.radius - ASTEROID_MIN_RADIUS
        self.new_asteroid = Asteroid(self.position.x, self.position.y, self.asteroid_new_radius)
        self.new_asteroid_2 = Asteroid(self.position.x, self.position.y, self.asteroid_new_radius)
        self.new_asteroid.velocity = velocity_1 * 1.2
        self.new_asteroid_2.velocity = velocity_2 * 1.2





