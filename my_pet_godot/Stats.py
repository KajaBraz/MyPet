import godot as gd

@gd.exposed
class Stats(gd.Node2D):
	def _ready(self):
		print(self.get_node("Node2D").scale)
		
	def _process(self, delta):
		self.decrease(0.1 * delta)
		
	def set_value(self, value):
		if val<0: val = 0
		if val>1: val = 1
#		self.get_node("Node2D").scale.x = val
		self.get_node("Node2D").scale = gd.Vector2(val, 1)
		
	def decrease(self, val):
		new_val = self.get_node("Node2D").scale.x - val
		if new_val > 0.01:
#			self.get_node("Node2D").scale.x = new_val
			self.get_node("Node2D").scale = gd.Vector2(new_val, 1)
