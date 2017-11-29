import sys

import pygame
import settings

from ship import Bullet
from alien import Alien

import star_field as sf

def check_keydown_events(event, game_settings, screen, ship, bullets):
	"""Key Press events"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(game_settings, screen, ship, bullets)
def check_keyup_events(event, ship):
	"""Key release events"""
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
def check_events(game_settings, screen, ship, bullets):
	"""Handles mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, game_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def update_screen(game_settings, screen, ship, aliens, bullets, star_field, clock, WHITE):
	#Update screen
	screen.fill(game_settings.bg_color)
	sf.deep_space(screen, star_field, clock, WHITE)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	#alien.blitme()
	aliens.draw(screen)
	#Display last drawn screen
	pygame.display.flip()

def update_bullets(bullets):
	bullets.update()
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def fire_bullet(game_settings, screen, ship, bullets):
	if len(bullets) < game_settings.bullet_amount:
		new_bullet = Bullet(game_settings, screen, ship)
		bullets.add(new_bullet)

def get_number_aliens_x(game_settings, alien_width):
		#Numbers of aliens in a row
		avialable_space_x = game_settings.screen_width - 2 * alien_width
		number_aliens_x = int(avialable_space_x / (2 * alien_width))
		return number_aliens_x

def create_alien(game_settings, screen, aliens, alien_number):
		#Create a single alien in a row
		alien = Alien(game_settings, screen)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		aliens.add(alien)

def create_fleet(game_settings, screen, aliens):
	"""Alien fleet appears"""
	alien = Alien(game_settings, screen)
	number_aliens_x = get_number_aliens_x(game_settings, alien.rect.width)
	#alien fleet 1st line
	for alien_number in range(number_aliens_x):
		create_alien(game_settings, screen, aliens, alien_number)
