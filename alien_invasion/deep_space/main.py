import pygame
import random

def run():
    screen = pygame.display.set_mode([800, 600])
    height = pygame.display.Info().current_h
    width = pygame.display.Info().current_w
    pygame.display.set_caption("Deep Space")
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)
    star_field = []
    clock = pygame.time.Clock()

    for stars in range(50):
        star_x = random.randrange(0, width)
        star_y = random.randrange(0, height)
        star_width = 5
        star_height = 5
        star_fill = random.randrange(0, 1)
        star_field.append([star_x, star_y, star_width, star_height])

    pygame.init()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()

        screen.fill(BLACK)

        for star in star_field:
            star[1] += 2
            if star[1] > height:
                star[0] = random.randrange(0, width)
                star[1] = random.randrange(-20, -5)
            pygame.draw.rect(screen, WHITE, star, 2)
            #pygame.draw.circle(screen, WHITE, star, 1)
        pygame.display.flip()
        clock.tick(30)
run()
