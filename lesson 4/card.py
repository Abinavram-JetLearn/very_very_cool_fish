import pygame, time
pygame.init()
WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
cakeimg = pygame.image.load("2. Pro Game Developer\lesson 4\cake.png")
cakeimg = pygame.transform.scale(cakeimg, (396, 510))

candle = pygame.image.load("2. Pro Game Developer\lesson 4\candle.png")
candle = pygame.transform.scale(candle, (50,100))

card = pygame.image.load("2. Pro Game Developer\lesson 4\card.jpg")
card = pygame.transform.scale(card, (448, 624))

font = pygame.font.SysFont("Arial", 36)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
    screen.fill("sky blue")
    screen.blit(card, (0,0))
    screen.blit(cakeimg, (25,0))
    pygame.display.update()
    time.sleep(2)
    screen.blit(candle, (200,20))
    pygame.display.update()
    time.sleep(2)
    text = font.render("Happy Father's day!", True, "red")
    screen.blit(text, (25,550))
    pygame.display.update()
    time.sleep(2)