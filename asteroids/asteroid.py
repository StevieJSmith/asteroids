from circleshape import CircleShape
import pygame
from constants import ASTEROID_MIN_RADIUS, ASTEROID_MAX_RADIUS
import random

class Asteroid(CircleShape):
   def __init__(self, x, y, radius):
      super().__init__(x, y, radius)
      self.image = pygame.Surface((self.radius*2, self.radius*2))
      self.image.set_colorkey((0,0,0))
      self.rect = self.image.get_rect()
      self.rect.center = (x, y)
      pygame.draw.circle(self.image, "white", (self.radius, self.radius), self.radius, 2)

   #def draw(self, screen):
   #   pygame.draw.circle(screen,"white", self.position, self.radius, 2)
   #   print(f"Drawing asteroid at: {self.position} with radius: {self.radius}")

   def update(self, dt):
      self.position += self.velocity * dt
      self.rect.center = self.position

   def split(self):
      self.kill()
      if self.radius <= ASTEROID_MIN_RADIUS:
         return

      random_angle = random.uniform(20, 50)
      first_velocity = self.velocity.rotate(-random_angle)
      second_velocity = self.velocity.rotate(random_angle)

      new_radius = self.radius - ASTEROID_MIN_RADIUS

      asteroid_one = Asteroid(self.rect.center[0], self.rect.center[1], new_radius)
      asteroid_two = Asteroid(self.rect.center[0], self.rect.center[1], new_radius)

      asteroid_one.velocity = first_velocity * 1.2
      asteroid_two.velocity = second_velocity * 1.2
