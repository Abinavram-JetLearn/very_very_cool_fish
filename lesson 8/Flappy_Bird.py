import pygame, random

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BG = pygame.image.load("2. Pro Game Developer\lesson 8\Bg.png")
BG = pygame.transform.scale(BG , (800, 600))

clock = pygame.time.Clock()

m_p = 0

platform = pygame.image.load("2. Pro Game Developer\lesson 8\ground.png")
platform = pygame.transform.scale(platform, (1600, 100))

player_anim_1 = pygame.image.load("2. Pro Game Developer\lesson 8\Bird_f1.png")
player_anim_2 = pygame.image.load("2. Pro Game Developer\lesson 8\Bird_f2.png")
player_anim_3 = pygame.image.load("2. Pro Game Developer\lesson 8\Bird_f3.png")

isGameOver = False
isFlying = False

class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.counter = 0
        self.vel = 0
        self.click = False
        self.images = [player_anim_1, player_anim_2, player_anim_3]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
    
    def update(self):
        if isFlying == True:
            if self.vel <= 8:
                self.vel += 0.3
            else:
                self.vel = 8
            if self.rect.bottom < 500:
                self.rect.y += self.vel
        if isGameOver == False:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE] and self.click == False and self.rect.top > 100:
                self.click = True
                self.vel = -10

            else:
                self.click = False

            if self.counter < 5:
                self.counter += 1
            else:
                self.counter = 0
                self.index += 1
                if self.index >= len(self.images):
                    self.index = 0

                self.image = self.images[self.index]

bird = Player(30,HEIGHT/2)
bird_Group = pygame.sprite.Group()
bird_Group.add(bird)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isFlying == False and isGameOver == False:
                    isFlying = True
    if bird.rect.bottom > 500:
        isGameOver = True

    if isGameOver == False:
        if bird.rect.top < 0:
            bird.rect.top = 0
        if m_p <= -800:
            m_p = 0
        else:
            m_p -= 0.1
    screen.blit(BG, (0,0))
    bird_Group.draw(screen)
    bird_Group.update()
    screen.blit(platform, (m_p, HEIGHT - 100))
    pygame.display.update()