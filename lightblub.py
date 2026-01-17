import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 400, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Light Bulb Switch")


BACKGROUND = (30, 30, 30)
OFF_COLOR = (100, 100, 100)
ON_COLOR = (255, 255, 0)
WHITE = (255, 255, 255)

bulb_radius = 50
bulb_pos = (WIDTH // 2, HEIGHT // 2)
light_on = False

font = pygame.font.SysFont(None, 30)

def draw_bulb():
    color = ON_COLOR if light_on else OFF_COLOR
    
    if light_on:
        for i in range(10):
            glow_radius = bulb_radius + (i * 5)
            alpha = max(0, 50 - (i * 5))
            glow_surf = pygame.Surface((glow_radius * 2, glow_radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surf, (*ON_COLOR, alpha), (glow_radius, glow_radius), glow_radius)
            screen.blit(glow_surf, (bulb_pos[0] - glow_radius, bulb_pos[1] - glow_radius))

    pygame.draw.circle(screen, color, bulb_pos, bulb_radius)
    pygame.draw.circle(screen, WHITE, bulb_pos, bulb_radius, 3)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos
            distance = ((mouse_x - bulb_pos[0])**2 + (mouse_y - bulb_pos[1])**2)**0.5
            if distance < bulb_radius:
                light_on = not light_on

    screen.fill(BACKGROUND)
    draw_bulb()
    
    text = font.render("Click the bulb to toggle", True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT - 50))
    
    pygame.display.flip()

pygame.quit()
sys.exit()