import sys

import pygame
import settings

def check_events(ship):
	"""Handles mouse events"""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				#Move right
				ship.moving_right = True
			elif event.key == pygame.K_LEFT:
				#Move left
				ship.moving_left = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				ship.moving_right = False
			elif event.key == pygame.K_LEFT:
				ship.moving_left = False
def update_screen(game_settings, screen, ship):
	#Update screen
	screen.fill(game_settings.bg_color)
	ship.blitme()
	#Display last drawn screen
	pygame.display.flip()