import pygame
from asteroidfield import AsteroidField
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot

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
   shots = pygame.sprite.Group()
   Shot.containers = (shots, updatable, drawable)

   print(f"Starting asteroids!")
   #print(f"Screen width: {SCREEN_WIDTH}")
   #print(f"Screen height: {SCREEN_HEIGHT}")

   kill_count = 0
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
            print(f"Final score: {kill_count}!")
            pygame.quit()

      for asteroid in asteroids:
         for shot in shots:
            if shot.collision(asteroid):
               shot.kill()
               asteroid.split()
               kill_count += 1

      dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
