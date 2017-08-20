import pygame

class Ship():
	def __init__(self, game_settings, screen):
		"""Инициирует корабль и задает его начальную позицию"""
		self.screen = screen
		self.game_settings = game_settings
		
		# Загрузка изображения корабля
		self.image = pygame.image.load('images/rocket.bmp')
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