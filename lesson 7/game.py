import pygame, random

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("2. Pro Game Developer\lesson 7\Bg.png")

player = pygame.image.load("2. Pro Game Developer\lesson 7\Trash.png")
player = pygame.transform.scale(player , (50, 75))

paper = pygame.image.load("2. Pro Game Developer\lesson 7\paper.png")
paper = pygame.transform.scale(paper , (50, 60))

box = pygame.image.load("2. Pro Game Developer\lesson 7\Box.png")

pencil = pygame.image.load("2. Pro Game Developer\lesson 7\pencil.png")

plastic = pygame.image.load("2. Pro Game Developer\lesson 7\plastic.png")
plastic = pygame.transform.scale(plastic , (50, 50))

item_list = [box, pencil, paper]

class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = player
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

class ReItems(pygame.sprite.Sprite):

    def __init__(self, x, y,):
        super().__init__()
        self.x = x
        self.y = y
        self.image = random.choice(item_list)
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

class NoItems(pygame.sprite.Sprite):

    def __init__(self, x, y,):
        super().__init__()
        self.x = x
        self.y = y
        self.image = plastic
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y

bin = Player(400, 300)
binGroup = pygame.sprite.Group()

recycleGroup = pygame.sprite.Group()

for i in range(30):
    reitem = ReItems(random.randint(50,1150), random.randint(50, 550))
    recycleGroup.add(reitem)

NonecycleGroup = pygame.sprite.Group()

for i in range (20):
    noitem = NoItems(random.randint(50,1150), random.randint(50, 550))
    NonecycleGroup.add(noitem)

binGroup.add(bin)

while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            bin.rect.center = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()

    screen.blit(bg, (0,0))
    binGroup.draw(screen)
    recycleGroup.draw(screen)
    NonecycleGroup.draw(screen)
    pygame.display.update()