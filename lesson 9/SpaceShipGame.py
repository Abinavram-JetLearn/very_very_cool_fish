import pygame, math, random

WIDTH = 800
HEIGHT = 600

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("2. Pro Game Developer\lesson 9\BG.png")
L_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\LargeAsteroid.png")
M_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\MediumAsteroid.png")
S_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\SmallAsteroid.png")
new_ship = pygame.image.load("2. Pro Game Developer\lesson 9\OtherShip.png")
ship = pygame.image.load("2. Pro Game Developer\lesson 9\Ship.png")
StarCollectable = pygame.image.load("2. Pro Game Developer\lesson 9\StarCollectable.png")

Big_Expo = pygame.mixer.Sound("2. Pro Game Developer\lesson 9\BangLarge.wav")
Small_Expo = pygame.mixer.Sound("2. Pro Game Developer\lesson 9\BangSmall.wav")
Shooting = pygame.mixer.Sound("2. Pro Game Developer\lesson 9\shoot.wav")

asteroids = [L_asteroid, M_asteroid, S_asteroid]

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.origional_image = ship
        self.image = self.origional_image
        self. rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.angle = 0
        self.speed = 5
    def update(self, keys):
        if keys[pygame.K_RIGHT]:
            self.angle -= 3
        if keys[pygame.K_LEFT]:
            self.angle +=  3
        if keys[pygame.K_UP]:
            rad = math.radians(self.angle + 90)
            self.rect.x += math.cos(rad) * self.speed
            self.rect.y -= math.sin(rad) * self.speed
        self.image = pygame.transform.rotate(self.origional_image, self.angle)
        self. rect = self.image.get_rect(center = self.rect.center)

class Asteroids(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = random.choice(asteroids)
        self.x = random.choice(WIDTH + random.randint(1,100), 0 - random.randint(1,100))
        self.y = random.choice(HEIGHT + random.randint(1,100), 0 - random.randint(1,100))
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)
        self.vx = random.randint(-4, 4)
        self.vy = random.randint(-4, 4)

    def update(self):
        self.rect.x = self.vx
        self.rect.y = self.vy


player = Spaceship()
player_group = pygame.sprite.Group()
player_group.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg, (0,0))
    keys = pygame.key.get_pressed()
    player_group.update(keys)
    player_group.draw(screen)
    pygame.display.update()