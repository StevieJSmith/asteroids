import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS, PLAYER_TURN_SPEED, PLAYER_SPEED

class Player(CircleShape, pygame.sprite.Sprite):
   def __init__(self, x, y):
      CircleShape.__init__(self, x,y, PLAYER_RADIUS)
      pygame.sprite.Sprite.__init__(self)
      self.rotation = 0
      surface_size = PLAYER_RADIUS * 2
      self.image = pygame.Surface((surface_size, surface_size))
      self.image.set_colorkey((0,0,0))
      self.rect = self.image.get_rect()

   # in the player class
   def triangle(self):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
      center = pygame.Vector2(self.rect.width/2, self.rect.height/2)
      a = center + forward * self.radius
      b = center - forward * self.radius - right
      c = center - forward * self.radius + right
      return [a, b, c]

   def draw(self):
      self.image.fill((0,0,0))
      pygame.draw.polygon(self.image, "white", self.triangle(), 2)

   def rotate(self, dt):
      self.rotation += PLAYER_TURN_SPEED * dt

   def update(self, dt):
      keys = pygame.key.get_pressed()

      if keys[pygame.K_a]:
         self.rotate(-dt)
      if keys[pygame.K_d]:
         self.rotate(dt)
      if keys[pygame.K_w]:
         self.move(dt)
      if keys[pygame.K_s]:
         self.move(-dt)
      self.draw()


   def move(self, dt):
      forward = pygame.Vector2(0, 1).rotate(self.rotation)
      self.position += forward * PLAYER_SPEED * dt
      self.rect.center = self.position
