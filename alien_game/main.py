import sys

import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship

def run_game():
	#Инициализация игры
	pygame.init()
	game_settings = Settings()
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	#Создадим корабль
	ship = Ship(game_settings, screen)
	
	#Bullet Group
	bullets = Group()

	# Запуск основного цикла игры
	while True:
		# Отслеживание событий 
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(game_settings, screen, ship, bullets)
run_game()