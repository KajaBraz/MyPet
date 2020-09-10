extends Area2D

export var speed = 10
var destination = 0
var moving_left = false

func _ready():
	$AnimatedSprite.play()
	pick_destination()

func _process(delta):
	if moving_left:
		position.x -= speed*delta
		if position.x < destination:
			pick_destination()
	else:
		position.x += speed*delta
		if position.x > destination:
			pick_destination()
	
func pick_destination():
	destination = rand_range(0, get_viewport_rect().size.x)
	print("los", destination)
	moving_left = false
	$AnimatedSprite.flip_h = false
	if destination < position.x:
		$AnimatedSprite.flip_h = true
		moving_left = true
