import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player

def main():
   pygame.init()
   clock = pygame.time.Clock()
   dt = 0
   x = SCREEN_WIDTH / 2
   y = SCREEN_HEIGHT / 2
   updatable = pygame.sprite.Group()
   drawable = pygame.sprite.Group()
   Player.containers = (updatable, drawable)
   player = Player(x, y)
   asteroids = pygame.sprite.Group()
   Asteroid.containers = (asteroids, updatable, drawable)
   AsteroidField.containers = (updatable,)
   asteroidfield = AsteroidField()
   print(f"Starting asteroids!")
   print(f"Screen width: {SCREEN_WIDTH}")
   print(f"Screen height: {SCREEN_HEIGHT}")

   screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

   while True:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            return
      screen.fill((50, 50, 50))  # Dark gray instead of black
      updatable.update(dt)
      drawable.draw(screen)
      pygame.display.flip()
      for asteroid in asteroids:
         if asteroid.collision(player):
            print("Game Over!")
            pygame.quit()
      dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
