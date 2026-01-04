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
        if self.y < 600 - self.r:
            u = self.vy
            self.vy += 2000 * dt
            self.y += (u + self.vy)* 0.5 * dt
            self.x += self.vx * dt
        else:
            self.y = HEIGHT - self.r
            self.vy = -self.vy * 0.9
    
    def Draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

ball1 = ball(25, 400,300,10, 20, "blue")
clock = pygame.time.Clock()
while True:
    dt = clock.tick(60) / 1000
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill("white")
    ball1.Draw()
    ball1.Acceleration(dt)
    pygame.display.update()