import sys

import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
import star_field as sf

def run_game():
	game_settings = Settings()
	clock = pygame.time.Clock()
	WHITE = (255, 255, 255)
	star_field = sf.background()

	pygame.init()
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	ship = Ship(game_settings, screen)
	bullets = Group()
	aliens = Group()
	# Запуск основного цикла игры
	while True:
		# Отслеживание событий
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(game_settings, screen, ship, aliens, bullets, star_field, clock, WHITE)
		clock.tick(60)
run_game()
