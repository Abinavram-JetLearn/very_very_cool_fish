import pygame, random

pygame.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

ship_w = 125
ship_h = 103.25

rocket1 = pygame.image.load("2. Pro Game Developer\lesson 6\ship1.png")
rocket1 = pygame.transform.rotate(rocket1, 90)
rocket1 = pygame.transform.scale(rocket1, (ship_w, ship_h))

rocket2 = pygame.image.load("2. Pro Game Developer\lesson 6\ship2.png")
rocket2 = pygame.transform.rotate(rocket2, 270)
rocket2 = pygame.transform.scale(rocket2, (ship_w, ship_h))

bg = pygame.image.load("2. Pro Game Developer\lesson 6\spacebg.png")
bg = pygame.transform.scale(bg, (1200,600))

border = pygame.Rect(WIDTH/2-5,0,10,HEIGHT)

class Ship(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        if self.color == "red":
            self.image = rocket1
        elif self.color == "yellow":
            self.image = rocket2
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.health = 100

    def move_ship(self, keys):
        if self.color == "red":
            if keys[pygame.K_w] and self.rect.y > -51.75:
                self.rect.y -= 1
            if keys[pygame.K_s] and self.rect.y < HEIGHT - 150:
                self.rect.y += 1
            if keys[pygame.K_a] and self.rect.x > -51.75:
                self.rect.x -= 1
            if keys[pygame.K_d] and self.rect.x < WIDTH / 2 -192.75:
                self.rect.x += 1
        elif self.color == "yellow":
            if keys[pygame.K_i] and self.rect.y > -51.75:
                self.rect.y -= 1
            if keys[pygame.K_k] and self.rect.y < HEIGHT - 150:
                self.rect.y += 1
            if keys[pygame.K_j] and self.rect.x > WIDTH / 2 - 55.75:
                self.rect.x -= 1
            if keys[pygame.K_l] and self.rect.x < WIDTH -192.75:
                self.rect.x += 1

class Bullets(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 50, 40)
    
    def update(self):
        if self.color == "yellow":
            if self.rect.x > 0:
                self.rect.x -= 2
            else:
                self.kill()

        if self.color == "red":
            if self.rect.x < WIDTH:
                self.rect.x += 2
            else:
                self.kill()

player1 = Ship("red", 100, HEIGHT / 2)
player2 = Ship("yellow", 1000, HEIGHT / 2)

red = pygame.sprite.Group()

yellow = pygame.sprite.Group()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                bullet = Bullets("red", player1.rect.x + ship_w, player1.rect.y + ship_h)
                red.add(bullet)
            if event.key == pygame.K_u:
                bullet = Bullets("yellow", player2.rect.x + ship_w, player2.rect.y + ship_h)
                yellow.add(bullet)

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, "red", border)
    screen.blit(player1.image, player1.rect.center)
    screen.blit(player2.image, player2.rect.center)
    for bullet in red:
        pygame.draw.rect(screen, "red", bullet.rect)

    for bullet in yellow:
        pygame.draw.rect(screen, "yellow", bullet.rect)

    red.update()
    yellow.update()
    
    keys = pygame.key.get_pressed()

    player1.move_ship(keys)
    player2.move_ship(keys)

    pygame.display.update()