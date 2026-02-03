import pygame, random, time

pygame.init()

WIDTH = 1200
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bg = pygame.image.load("2. Pro Game Developer\lesson 7\Bg.png")
bg = pygame.transform.scale(bg, (1200, 800))

player = pygame.image.load("2. Pro Game Developer\lesson 7\Trash.png")
player = pygame.transform.scale(player , (50, 75))

paper = pygame.image.load("2. Pro Game Developer\lesson 7\paper.png")
paper = pygame.transform.scale(paper , (50, 60))

box = pygame.image.load("2. Pro Game Developer\lesson 7\Box.png")

pencil = pygame.image.load("2. Pro Game Developer\lesson 7\pencil.png")

plastic = pygame.image.load("2. Pro Game Developer\lesson 7\plastic.png")
plastic = pygame.transform.scale(plastic , (50, 50))

item_list = [box, pencil, paper]

score = 0

font = pygame.font.SysFont("Verdana", 36)

clock = pygame.time.Clock()
start_time = time.time()

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
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            bin.rect.center = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            pygame.quit()
    
    if time.time() - start_time >= 10:
        if score >= 25:
            score_text = font.render("Well Done", font, "white")
            screen.blit(score_text, (100, 250))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()
        else:
            score_text = font.render("You Failed!", font, "white")
            screen.blit(score_text, (100, 250))
            pygame.display.update()
            time.sleep(3)
            pygame.quit()

    screen.blit(bg, (0,0))
    score_text = font.render(f"Score: {score}", font, "white")
    screen.blit(score_text, (100, 50))
    recycleGroup_items = pygame.sprite.spritecollide(bin, recycleGroup, True)
    for item in recycleGroup_items:
        score +=1
    NonecycleGroup_items = pygame.sprite.spritecollide(bin, NonecycleGroup, True)
    for items in NonecycleGroup_items:
        score -= 1
    binGroup.draw(screen)
    recycleGroup.draw(screen)
    NonecycleGroup.draw(screen)
    pygame.display.update()