import pygame, math, random, time

WIDTH = 800
HEIGHT = 600
clock = pygame.time.Clock()

count = 0

pygame.init()

score = 0

font = pygame.font.SysFont("Verdana", 36)

screen = pygame.display.set_mode((WIDTH, HEIGHT))

game_State = True

bg = pygame.image.load("2. Pro Game Developer\lesson 9\BG.png")
L_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\LargeAsteroid.png")
M_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\MediumAsteroid.png")
S_asteroid = pygame.image.load("2. Pro Game Developer\lesson 9\SmallAsteroid.png")
new_ship = pygame.image.load("2. Pro Game Developer\lesson 9\OtherShip.png")
ship = pygame.image.load("2. Pro Game Developer\lesson 9\Ship.png")
ship = pygame.transform.scale(ship, (85, 50))
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
        self.health = 10
    def update(self, keys, bullet_group, player_group):
        if keys[pygame.K_RIGHT]:
            self.angle -= 3
        if keys[pygame.K_LEFT]:
            self.angle +=  3
        if keys[pygame.K_UP]:
            rad = math.radians(self.angle + 90)
            self.rect.x += math.cos(rad) * self.speed
            self.rect.y -= math.sin(rad) * self.speed
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0
        if self.rect.top < -100:
            self.rect.bottom = HEIGHT + 100
        if self.rect.bottom > HEIGHT + 100:
            self.rect.top = -100
        self.image = pygame.transform.rotate(self.origional_image, self.angle)
        self.rect = self.image.get_rect(center = self.rect.center)

    def Shoot(self, bullet_group, player_group):
            bullet = Bullet(self.rect.center, self.angle)
            bullet_group.add(bullet)

class Asteroids(pygame.sprite.Sprite):
    def __init__(self, player, asteroid_group):
        super().__init__()
        self.image = random.choice(asteroids)
        self.group = asteroid_group
        self.x = random.choice([WIDTH + random.randint(-50,100), 0 - random.randint(-50,100)])
        self.y = random.choice([HEIGHT + random.randint(-50,100), 0 - random.randint(-50,100)])
        self.rect = self.image.get_rect()
        self.player = player
        self.rect.center = (self.x, self.y)
        self.speed = random.randint(1,6)
        dx = self.player.rect.x - self.rect.x
        dy = self.player.rect.y - self.rect.y
        distance = math.hypot(dx,dy)
        if distance != 0:
            dx/= distance
            dy/= distance
        self.vx = dx* self.speed
        self.vy = dy* self.speed

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if not screen.get_rect().inflate(100,100).colliderect(self.rect):
            self.kill()

        if pygame.sprite.spritecollide(player, self.group, True):
            self.player.health -= 1
            Small_Expo.play()
            self.kill()

player = Spaceship()
player_group = pygame.sprite.Group()
player_group.add(player)
asteroid_group = pygame.sprite.Group()
bullet_group = pygame.sprite.Group()

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, angle):
        super().__init__()
        self.image = pygame.Surface((4,4))
        self.image.fill((230, 23, 106))
        self.rect = self.image.get_rect(center=pos)
        rad = math.radians(angle+90)
        self.vx = math.cos(rad)*10
        self.vy = -math.sin(rad)*10
    
    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if not screen.get_rect().colliderect(self.rect):
            self.kill()

while game_State == True:
    clock.tick(60)
    count += 1
    text = font.render(f"Lives: {player.health} Score: {score}", True, "white")
    if count == 60:
        asteroid = Asteroids(player, asteroid_group)
        asteroid_group.add(asteroid)
        count = 0
    hitlist = pygame.sprite.groupcollide(bullet_group, asteroid_group, True, True)
    for item in hitlist:
        score += random.randint(1,10)
        Big_Expo.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.Shoot(bullet_group, player_group)
                Shooting.play()


    if player.health < 1:
        game_State = False
        text = font.render(f"You got! {score} Point(s)! Press 'R' to Restart", True, "white")
        screen.blit(bg, (0,0))
        screen.blit(text, (0,0))
        pygame.display.update()
        time.sleep(3)
        if keys[pygame.K_r]:
            if game_State == False:
                game_State = True
                player.health = 10
                score = 0
                for asteroid in asteroid_group:
                    asteroid.kill()

    screen.blit(bg, (0,0))
    screen.blit(text, (0,0))
    keys = pygame.key.get_pressed()
    player_group.update(keys, bullet_group, player_group)
    player_group.draw(screen)
    asteroid_group.draw(screen)
    asteroid_group.update()
    bullet_group.update()
    bullet_group.draw(screen)
    pygame.display.update()
