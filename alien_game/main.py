import sys

import pygame

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

	# Запуск основного цикла игры
	while True:
		# Отслеживание событий 
		gf.check_events(ship)
		ship.update()
		gf.update_screen(game_settings, screen, ship)
			
run_game()