import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""Single alien class"""
	def __init__(self, game_settings, screen):
		"""Init alien and sets default position"""
		super(Alien, self).__init__()
		self.screen = screen
		self.game_settings = game_settings

		#Loading alien image
		self.image = pygame.image.load('images/invader.png')
		self.rect = self.image.get_rect()

		#Every alien will appear in the top left corner
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		#Accurate position of the alien
		self.x = float(self.rect.x)

	def update(self):
		self.x += (self.game_settings.aliens_speed *
			self.game_settings.aliens_direction)
		self.rect.x = self.x


	def blitme(self):
		self.screen.blit(self.image, self.rect)

	def check_edge(self):
		screen_rect = self.screen.get_rect()
