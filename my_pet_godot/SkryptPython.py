import godot as gd

@gd.exposed
class SkryptPython(gd.Polygon2D):
	# member variables here, example:
	a = gd.export(int, default=150)
	b = gd.export(str, default='foo')
	Pole = gd.export(int, default=333)
	pole2 = gd.export(int, default=450)

	x = 13

	def _ready(self):
		"""
		Called every time the node is added to the scene.
		Initialization here.
		"""
		print(f"Oto python! {self.get_node('polygon2d')} {self.a} {self.b} {self.Pole} {self.pole2}")
