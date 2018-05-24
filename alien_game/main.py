import sys

import pygame
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship
#from alien import Alien

import star_field as sf

def run_game():
	game_settings = Settings()
	clock = pygame.time.Clock()
	WHITE = (255, 255, 255)
	star_field = sf.background()

	#Инициализация игры
	pygame.init()
	screen = pygame.display.set_mode(
		(game_settings.screen_width, game_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	#Создадим корабль
	ship = Ship(game_settings, screen)
	#Create an alien
	#alien = Alien(game_settings, screen)
	#Bullet Group
	bullets = Group()
	#Alliens fleet
	aliens = Group()
	gf.create_fleet(game_settings, screen, aliens, ship)
	# Запуск основного цикла игры
	while True:
		# Отслеживание событий
		gf.check_events(game_settings, screen, ship, bullets)
		ship.update()
		gf.update_bullets(aliens, bullets)
		gf.update_aliens(aliens, game_settings)
		gf.update_screen(game_settings, screen, ship, aliens, bullets, star_field, clock, WHITE)
		clock.tick(60)
run_game()
