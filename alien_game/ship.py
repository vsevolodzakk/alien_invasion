import pygame
from pygame.sprite import Sprite

class Ship():
	def __init__(self, game_settings, screen):
		"""Инициирует корабль и задает его начальную позицию"""
		self.screen = screen
		self.game_settings = game_settings
		
		# Загрузка изображения корабля
		self.image = pygame.image.load('images/rocket.png')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		#
		self.rect.centerx = self.screen_rect.centerx
		self.rect.bottom = self.screen_rect.bottom
		
		#Saving ship center coordiantes
		self.center = float(self.rect.centerx)
		
		#Movement flag
		self.moving_right = False
		self.moving_left = False
	def update(self):
		"""Updates position according to flag state"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.center += self.game_settings.ship_speed_factor
		if self.moving_left and self.rect.left > 0:
			self.center -= self.game_settings.ship_speed_factor
		self.rect.centerx = self.center	
	def blitme(self):
		"""Рисует кораблю в текущей позиции"""
		self.screen.blit(self.image, self.rect)
		
class Bullet(Sprite):
	def __init__(self, game_settings, screen, ship):
		"""Bullet object appears"""
		super().__init__()
		self.screen = screen
		
		#Bullet creation in (0,0) position
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top
		
		#Bullet center coordiantes
		self.y = float(self.rect.y)
		
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		
	def update(self):
		"""Translate bullet on the screen"""
		#Bullet position update in float
		self.y -= self.speed
		#Rect position update
		self.rect.y = self.y
	def draw_bullet(self):
		"""Bullet on the screen"""
		pygame.draw.rect(self.screen, self.color, self.rect)