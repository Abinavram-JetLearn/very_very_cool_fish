import pygame, random

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = pygame.image.load("2. Pro Game Developer\lesson 5\space.png")
rocket = pygame.image.load("2. Pro Game Developer\lesson 5\spaceship.png")
rocket = pygame.transform.scale(rocket, (54, 100))

class Rocket(pygame.sprite.Sprite):
    def __init__(self, posx, posy, image):
        super().__init__()
        self.x = posx
        self.y = posy
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
    def Move(self, keys):
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= 1
        if keys[pygame.K_s] and self.rect.y < HEIGHT - 100:
            self.rect.y += 1
        if keys[pygame.K_a] and self.rect.x > 0:
            self.rect.x -= 1
        if keys[pygame.K_d] and self.rect.x < WIDTH - 54:
            self.rect.x += 1

r1 = Rocket(400,300,rocket)
rocket_group = pygame.sprite.Group()
rocket_group.add(r1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        

    keys = pygame.key.get_pressed()

    rocket_group.draw(screen)
    r1.Move(keys)
    pygame.display.update()