import pygame
import random

from settings import Settings

def background():
    star_field = []
    for stars in range(50):
        star_x = random.randrange(0, 800)
        star_y = random.randrange(0, 600)
        star_width = 5
        star_height = 5
        star_field.append([star_x, star_y, star_width, star_height])
    return(star_field)
def deep_space(screen, star_field, clock, WHITE):
	star_fill = 0
	for star in star_field:
		star[1] += 2
		if star[1] > 600:
			star[0] = random.randrange(0, 800)
			star[1] = random.randrange(-10, -5)
		pygame.draw.rect(screen, WHITE, star, star_fill)

		#clock.tick(60)
