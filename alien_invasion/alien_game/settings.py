class Settings():
	"""Класс настроек игры."""
	def __init__(self):
		"""Инициализация настроек."""
		# Параметры экрана
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0, 0, 0)

		#Ship settings
		self.ship_speed_factor = 0.5

		#Bullet settings
		self.bullet_speed = 0.7
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_amount = 3
