import pygame

class Ship():
	def __init__(self, screen):
		"""Инициирует корабль и задает его начальную позицию"""
		self.screen = screen
		
		# Загрузка изображения корабля
		self.image = pygame.image.load('images/rocket.bmp')
		self.rect = self.image.get_rect()
		#
		self.rect.centerx = self.screen.rect.centerx
		self.rect.bottom = self.screen_rect.bottom
	def blitme(self):
		"""Рисует кораблю в текущей позиции"""
		self.screen.blit(self.image, self.rect)