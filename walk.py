import turtle
import math


# Window setup
screen = turtle.Screen()
screen.title("Arrow Key Sprite Walk")
screen.bgcolor("black")
screen.setup(width=800, height=600)


def make_sprite_points(direction):
	"""Return polygon points for a small rocket-like sprite in a direction."""
	right_points = [
		(22, 0),
		(5, 10),
		(5, 5),
		(-14, 5),
		(-14, -5),
		(5, -5),
		(5, -10),
	]

	def rotate(points, degrees):
		radians = math.radians(degrees)
		cos_a = math.cos(radians)
		sin_a = math.sin(radians)
		return [
			(
				round(x * cos_a - y * sin_a),
				round(x * sin_a + y * cos_a),
			)
			for x, y in points
		]

	rotation_by_direction = {
		"right": 0,
		"up": 90,
		"left": 180,
		"down": -90,
	}
	return rotate(right_points, rotation_by_direction[direction])


def register_sprite_shape(name, points):
	shape = turtle.Shape("polygon", points)
	screen.register_shape(name, shape)


# Register 4 direction frames (sprite shapes)
register_sprite_shape("sprite_up", make_sprite_points("up"))
register_sprite_shape("sprite_down", make_sprite_points("down"))
register_sprite_shape("sprite_left", make_sprite_points("left"))
register_sprite_shape("sprite_right", make_sprite_points("right"))


player = turtle.Turtle()
player.penup()
player.speed(0)
player.color("cyan")
player.shape("sprite_down")
# Compensate turtle's polygon orientation offset so frame names match arrow keys.
player.setheading(90)

STEP = 20


def move_up():
	player.shape("sprite_up")
	player.sety(player.ycor() + STEP)


def move_down():
	player.shape("sprite_down")
	player.sety(player.ycor() - STEP)


def move_left():
	player.shape("sprite_left")
	player.setx(player.xcor() - STEP)


def move_right():
	player.shape("sprite_right")
	player.setx(player.xcor() + STEP)


screen.listen()
screen.onkeypress(move_up, "Up")
screen.onkeypress(move_down, "Down")
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

turtle.done()
