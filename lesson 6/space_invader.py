import pygame, random

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

rocket1 = pygame.image.load("2. Pro Game Developer\lesson 6\ship1.png")
rocket1 = pygame.transform.rotate(rocket1, 270)
rocket1 = pygame.transform.scale(rocket1, (125,103.25))

rocket2 = pygame.image.load("2. Pro Game Developer\lesson 6\ship2.png")
rocket2 = pygame.transform.rotate(rocket2, 90)
rocket2 = pygame.transform.scale(rocket2, (125,103.25))

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
            if keys[pygame.K_s] and self.rect.y < HEIGHT - 40:
                print(self.rect.y)
                self.rect.y += 1
            if keys[pygame.K_a]:
                self.rect.x -= 1
            if keys[pygame.K_d]:
                self.rect.x += 1
        elif self.color == "yellow":
            if keys[pygame.K_UP] and self.rect.y > -51.75:
                self.rect.y -= 1
            if keys[pygame.K_DOWN]:
                self.rect.y += 1
            if keys[pygame.K_LEFT]:
                self.rect.x -= 1
            if keys[pygame.K_RIGHT]:
                self.rect.x += 1

player1 = Ship("red", 100, 100)
player2 = Ship("yellow", 500, 100)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.blit(bg, (0,0))
    pygame.draw.rect(screen, "red", border)
    screen.blit(player1.image, player1.rect.center)
    screen.blit(player2.image, player2.rect.center)
    keys = pygame.key.get_pressed()

    player1.move_ship(keys)
    player2.move_ship(keys)

    pygame.display.update()