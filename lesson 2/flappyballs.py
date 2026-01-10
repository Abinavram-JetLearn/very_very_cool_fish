import pygame

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class ball():

    def __init__(self, radius, posx, posy, vx, vy, colour):
        self.r = radius
        self.x = posx
        self.y = posy
        self.vx = vx
        self.vy = vy
        self.color = colour
    
    def Acceleration(self, dt):
        u = self.vy
        self.vy += 2000 * dt
        self.y += (u + self.vy)* 0.5 * dt
        #self.x += self.vx * dt
        if self.y > HEIGHT - self.r:
            self.y = HEIGHT - self.r
            self.vy = -self.vy * 0.9
    
    def Draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)
ball1 = ball(25, 400,50,10, 40, "blue")
ball2 = ball(50, 300,100,15, 20, "red")
ball3 = ball(10, 500,25,5, 30, "green")
clock = pygame.time.Clock()
while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                ball1.vy = -1000
                ball2.vy = -500
                ball3.vy = -750
    screen.fill("white")
    ball1.Draw()
    ball2.Draw()
    ball3.Draw()
    ball1.Acceleration(dt)
    ball2.Acceleration(dt)
    ball3.Acceleration(dt)
    pygame.display.update()