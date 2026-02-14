import pygame, random, time

pygame.init()

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

restart_button = pygame.image.load("2. Pro Game Developer\lesson 8\Restart.png")

font = pygame.font.SysFont("Verdana", 36)

pipe_img = pygame.image.load("2. Pro Game Developer\lesson 8\pipe.png")

isGameOver = False
isFlying = False

pipe_gap = 150
pipe_frequency = 1500
last_pipe = pygame.time.get_ticks()

restart_button_x = WIDTH/2 - 60
restart_button_y = HEIGHT/2 - 42

score = 0

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
                self.vel = -5

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

class Pipe (pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        super().__init__()
        self.x = x
        self.y = y
        self.dir = direction
        self.image = pipe_img
        self.rect = self.image.get_rect()
        if self.dir == "top":
            self.image = pygame.transform.flip(self.image, False, True)
            self.rect.bottomleft = self.x, self.y - pipe_gap/2
        if self.dir == "bottom":
            self.rect.topleft = self.x, self.y + pipe_gap/2
    
    def update(self):
        if self.rect.x > -78:
            self.rect.x -= 3
        else:
            self.kill()

pipe_group = pygame.sprite.Group()
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if isGameOver == True and pygame.mouse.get_pos()[0] >= restart_button_x and pygame.mouse.get_pos()[0] <= restart_button_x + 1200 and pygame.mouse.get_pos()[1] >= restart_button_y and pygame.mouse.get_pos()[1] <= restart_button_y + 42:
                isGameOver = False
                pipe_group.empty()
                bird.rect.x = 30
                bird.rect.y = HEIGHT/2
                isFlying = False
                score = 0

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if isFlying == False and isGameOver == False:
                    isFlying = True
    if bird.rect.bottom > 500:
        isGameOver = True

    if pygame.sprite.groupcollide(bird_Group, pipe_group, False, False):
        isGameOver = True

    if isGameOver == False:
        pipe_group.update()
        time_now = pygame.time.get_ticks()
        if time_now - last_pipe > pipe_frequency:
            y = random.randint(-100,100)
            bottompipe = Pipe(WIDTH, HEIGHT/2 + y, "bottom")
            toppipe = Pipe(WIDTH, HEIGHT/2 + y, "top")
            pipe_group.add(bottompipe)
            pipe_group.add(toppipe)
            last_pipe = time_now 
        if bird.rect.top < 0:
            bird.rect.top = 0
        if m_p <= -800:
            m_p = 0
        else:
            m_p -= 3
        for pipes in pipe_group:
            if pipes.rect.x < -70:
                score += 0.5
                pipes.kill()

    screen.blit(BG, (0,0))
    bird_Group.draw(screen)
    pipe_group.draw(screen)
    bird_Group.update()
    screen.blit(platform, (m_p, HEIGHT - 100))
    scoremsG = f"Score: {int(score)}"
    scoremsg = font.render(scoremsG, True, True)
    screen.blit(scoremsg, (10,10))
    if isGameOver == True:
        restart_msg = "Game Over! Press Restart!"
        screen.blit(restart_button, (restart_button_x, restart_button_y))
        text = font.render(restart_msg, True, True)
        screen.blit(text, (225,10))
    pygame.display.update()