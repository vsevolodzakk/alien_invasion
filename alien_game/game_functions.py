import sys

import pygame
import settings

from ship import Bullet

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

def update_screen(game_settings, screen, ship, bullets):
	#Update screen
	screen.fill(game_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
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