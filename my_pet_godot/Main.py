import godot as gd

@gd.exposed
class Main(gd.Node2D):
	speed = gd.export(float, default=0.1)
	
	def _ready(self):
		pass
	
#	def _process(self, delta):
#		val = self.speed * delta
#		self.get_node("Stat1").decrease(val)
#		self.get_node("Stat2").decrease(val)
#		self.get_node("Stat3").decrease(val)
#		self.get_node("Stat4").decrease(val)
