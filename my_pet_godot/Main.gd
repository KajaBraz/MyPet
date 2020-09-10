extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
export var speed = 0.1

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var val = speed * delta
	$Stat1.decrease(val)
	$Stat2.decrease(val)
	$Stat3.decrease(val)
	$Stat4.decrease(val)
