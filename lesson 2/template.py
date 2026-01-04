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

class circle():

    def __init__(self, radius, posx, posy, colour):
        self.r = radius
        self.x = posx
        self.y = posy
        self.color = colour
    
    def Draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

rect1 = rectangle(100,200,100,200,"blue")
rectran = rectangle(random.randint(100,200),random.randint(100,200),200,200,"green")
circ2 = circle(100, 100, 400, "red")
circran = circle(random.randint(100,200), 500, 400, "purple")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.fill("sky blue")
    rect1.Draw()
    circ2.Draw()
    rectran.Draw()
    circran.Draw()
    pygame.display.update()