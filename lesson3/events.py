import pygame, random

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

class rectangle():

    def __init__(self, length, width, posx, posy, colour):
        self.length = length
        self.width = width
        self.x = posx
        self.y = posy
        self.color = colour
    
    def Draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.length))

    def Grow(self):
        self.length *= 2
        self.width *= 2

class circle():

    def __init__(self, radius, posx, posy, colour):
        self.r = radius
        self.x = posx
        self.y = posy
        self.color = colour
    
    def Draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

rect1 = rectangle(100,200,200,200,"green")

screen.fill("sky blue")
pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            rect1.Draw()
            pygame.display.update()
        if event.type == pygame.MOUSEBUTTONUP:
            rect1.Grow()
            pygame.display.update()
        if event.type == pygame.MOUSEMOTION:
            pos = pygame.mouse.get_pos()
            circ1 = circle(1, pos[0], pos[1], "red")
            circ1.Draw()
            pygame.display.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                pos = pygame.mouse.get_pos()
                circ1 = circle(5, pos[0], pos[1], "blue")
                circ1.Draw()
                pygame.display.update()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_F1:
                pos = pygame.mouse.get_pos()
                circ1 = circle(1, pos[0], pos[1], "red")
                circ1.Draw()
                pygame.display.update()
                pygame.draw.ellipse(screen, "yellow", (random.randint(50,100), random.randint(50,100), random.randint(100,HEIGHT-100), random.randint(100,WIDTH-100)))
#ellipse(surface, color, rect) -> Rect