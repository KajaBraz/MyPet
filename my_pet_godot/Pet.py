import godot as gd
import random

@gd.exposed
class Pet(gd.Area2D):
	def _ready(self):
		self.speed = 20
		self.destination = 0
		self.moving_left = False
		self.get_node("AnimatedSprite").play()
		self.pick_destination()

	def _process(self, delta):
		if self.moving_left:
#			self.position.x -= self.speed * delta
			self.position = gd.Vector2(self.position.x - self.speed * delta, self.position.y)
			if self.position.x < self.destination:
				self.pick_destination()
		else:
#			self.position.x += self.speed * delta
			self.position = gd.Vector2(self.position.x + self.speed * delta, self.position.y)
			if self.position.x > self.destination:
				self.pick_destination()
	
	def pick_destination(self):
		self.destination = random.randrange(0, self.get_viewport_rect().size.x)
		print("los", self.destination)
		self.moving_left = False
		self.get_node("AnimatedSprite").flip_h = False
		if self.destination < self.position.x:
			self.get_node("AnimatedSprite").flip_h = True
			self.moving_left = True
