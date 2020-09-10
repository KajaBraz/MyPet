extends Node2D

# Called when the node enters the scene tree for the first time.
func _ready():
	print($Node2D.scale.x)

func set_value(val):
	if val<0: val = 0
	if val>1: val = 1
	$Node2D.scale.x = val

func decrease(val):
	var new_val = $Node2D.scale.x - val
	if new_val > 0.01:
		$Node2D.scale.x = new_val
