class Settings():
	"""Класс настроек игры."""
	def __init__(self):
		"""Инициализация настроек."""
		# Параметры экрана
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (0, 0, 0)

		#Ship settings
		self.ship_speed_factor = 2

		#Bullet settings
		self.bullet_speed = 6
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_amount = 3

		#Fleet settings
		self.aliens_speed = 2
		self.aliens_direction = -1
		#self.advance_value = 10
