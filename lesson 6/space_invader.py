import pygame, random, time

pygame.init()
pygame.mixer.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.SysFont("Verdana", 36)

clock = pygame.time.Clock()

grenade = pygame.mixer.Sound("2. Pro Game Developer\lesson 6\Grenade+1.mp3")
gun = pygame.mixer.Sound("2. Pro Game Developer\lesson 6\Gun+Silencer.mp3")

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
                self.rect.y -= 2
            if keys[pygame.K_s] and self.rect.y < HEIGHT - 150:
                self.rect.y += 2
            if keys[pygame.K_a] and self.rect.x > -51.75:
                self.rect.x -= 2
            if keys[pygame.K_d] and self.rect.x < WIDTH / 2 -192.75:
                self.rect.x += 2
        elif self.color == "yellow":
            if keys[pygame.K_i] and self.rect.y > -51.75:
                self.rect.y -= 2
            if keys[pygame.K_k] and self.rect.y < HEIGHT - 150:
                self.rect.y += 2
            if keys[pygame.K_j] and self.rect.x > WIDTH / 2 - 55.75:
                self.rect.x -= 2
            if keys[pygame.K_l] and self.rect.x < WIDTH -192.75:
                self.rect.x += 2

class Bullets(pygame.sprite.Sprite):
    def __init__(self, color, x, y):
        super().__init__()
        self.color = color
        self.x = x
        self.y = y
        self.rect = pygame.Rect(self.x, self.y, 20, 10)
    
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

winner = ""

while True:

    clock.tick(120)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q and len(red) < 5:
                bullet = Bullets("red", player1.rect.x + ship_w, player1.rect.y + ship_h)
                red.add(bullet)
                gun.play()
            if event.key == pygame.K_u and len(yellow) < 5:
                bullet = Bullets("yellow", player2.rect.x + ship_w, player2.rect.y + ship_h)
                yellow.add(bullet)
                gun.play()

    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, "red", border)

    health_p1 = font.render(f"Red Health: {player1.health}", True, "white")
    
    health_p2 = font.render(f"Yellow Health: {player2.health}", True, "white")
    
    if player1.health < 1:
        winner = font.render("Yellow Wins!!!", True, "white")
        screen.blit(winner, (WIDTH/2, 100))
        pygame.display.update()
        time.sleep(3)
        pygame.quit()
    elif player2.health < 1:
        winner = font.render("Red Wins!!!", True, "white")
        screen.blit(winner, (WIDTH/2, 100))
        time.sleep(3)
        pygame.quit()

    screen.blit(health_p1, (100, 10))
    screen.blit(health_p2, (800, 10))

    screen.blit(player1.image, player1.rect.center)
    screen.blit(player2.image, player2.rect.center)

    for bullet in red:
        pygame.draw.rect(screen, "red", bullet.rect)

    for bullet in yellow:
        pygame.draw.rect(screen, "yellow", bullet.rect)

    for bullet in red:
        if bullet.rect.colliderect(player2.rect):
            player2.health -= 5
            bullet.kill()
            grenade.play()

    for bullet in yellow:
        if bullet.rect.colliderect(player1.rect):
            player1.health -= 5
            bullet.kill()
            grenade.play()

    red.update()
    yellow.update()
    
    keys = pygame.key.get_pressed()

    player1.move_ship(keys)
    player2.move_ship(keys)

    pygame.display.update()