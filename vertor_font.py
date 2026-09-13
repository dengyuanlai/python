import turtle


# Segment endpoints in a normalized character box (width=60, height=100).
SEGMENT_LINES = {
	"a": ((10, 100), (50, 100)),
	"b": ((50, 95), (50, 55)),
	"c": ((50, 45), (50, 5)),
	"d": ((10, 0), (50, 0)),
	"e": ((10, 45), (10, 5)),
	"f": ((10, 95), (10, 55)),
	"g1": ((10, 50), (30, 50)),
	"g2": ((30, 50), (50, 50)),
	"h": ((10, 95), (30, 55)),
	"i": ((50, 95), (30, 55)),
	"j": ((10, 5), (30, 45)),
	"k": ((50, 5), (30, 45)),
	"l": ((30, 95), (30, 55)),
	"m": ((30, 45), (30, 5)),
}


# Vector font map: each character maps to a list of segment keys above.
FONT_SEGMENTS = {
	"A": ["a", "b", "c", "e", "f", "g1", "g2"],
	"B": ["f", "e", "d", "c", "b", "g1", "g2", "l", "m"],
	"C": ["a", "f", "e", "d"],
	"D": ["b", "c", "d", "e", "g1", "g2", "l", "m"],
	"E": ["a", "f", "e", "d", "g1", "g2"],
	"F": ["a", "f", "e", "g1", "g2"],
	"G": ["a", "f", "e", "d", "c", "g2"],
	"H": ["f", "e", "b", "c", "g1", "g2"],
	"I": ["a", "d", "l", "m"],
	"J": ["b", "c", "d", "e"],
	"K": ["f", "e", "g1", "h", "k"],
	"L": ["f", "e", "d"],
	"M": ["f", "b", "e", "c", "h", "i"],
	"N": ["f", "b", "e", "c", "i", "j"],
	"O": ["a", "b", "c", "d", "e", "f"],
	"P": ["a", "b", "f", "e", "g1", "g2"],
	"Q": ["a", "b", "c", "d", "e", "f", "k"],
	"R": ["a", "b", "f", "e", "g1", "g2", "k"],
	"S": ["a", "f", "g1", "g2", "c", "d"],
	"T": ["a", "l", "m"],
	"U": ["f", "e", "d", "c", "b"],
	"V": ["f", "e", "j", "k"],
	"W": ["f", "e", "c", "b", "j", "k"],
	"X": ["h", "i", "j", "k"],
	"Y": ["h", "i", "m"],
	"Z": ["a", "i", "j", "d"],
	"0": ["a", "b", "c", "d", "e", "f"],
	"1": ["b", "c"],
	"2": ["a", "b", "g1", "g2", "e", "d"],
	"3": ["a", "b", "g1", "g2", "c", "d"],
	"4": ["f", "g1", "g2", "b", "c"],
	"5": ["a", "f", "g1", "g2", "c", "d"],
	"6": ["a", "f", "g1", "g2", "c", "d", "e"],
	"7": ["a", "b", "c"],
	"8": ["a", "b", "c", "d", "e", "f", "g1", "g2"],
	"9": ["a", "b", "c", "d", "f", "g1", "g2"],
	"-": ["g1", "g2"],
	".": ["dot"],
	" ": [],
	"?": ["a", "b", "g2", "m", "dot"],
}


CHAR_WIDTH = 60
CHAR_HEIGHT = 100
CHAR_ADVANCE = 75


def draw_segment(pen: turtle.Turtle, segment: str, x_offset: float, y_offset: float, scale: float) -> None:
	if segment == "dot":
		pen.penup()
		pen.goto(x_offset + 54 * scale, y_offset - 10 * scale)
		pen.pendown()
		pen.begin_fill()
		pen.circle(3.5 * scale)
		pen.end_fill()
		return

	start, end = SEGMENT_LINES[segment]
	x1 = x_offset + start[0] * scale
	y1 = y_offset + start[1] * scale
	x2 = x_offset + end[0] * scale
	y2 = y_offset + end[1] * scale

	pen.penup()
	pen.goto(x1, y1)
	pen.pendown()
	pen.goto(x2, y2)


def draw_text_vector(text: str, led_color: str = "#5CF2FF") -> None:
	screen = turtle.Screen()
	screen.title("Vector LED Font")
	screen.bgcolor("#05080D")
	screen.setup(width=1200, height=360)
	screen.tracer(6, 100)

	pen = turtle.Turtle()
	pen.hideturtle()
	pen.speed(0)
	pen.pensize(7)
	pen.color(led_color)

	safe_text = text.upper() if text else "?"
	count = len(safe_text)
	scale = min(1.0, 12 / max(count, 1))

	total_width = (count * CHAR_ADVANCE - (CHAR_ADVANCE - CHAR_WIDTH)) * scale
	start_x = -total_width / 2
	baseline_y = -CHAR_HEIGHT * scale / 2

	for index, char in enumerate(safe_text):
		x_offset = start_x + index * CHAR_ADVANCE * scale
		segments = FONT_SEGMENTS.get(char, FONT_SEGMENTS["?"])
		for segment in segments:
			draw_segment(pen, segment, x_offset, baseline_y, scale)

	screen.update()
	screen.mainloop()


def main() -> None:
	message = input("Input text: ")
	draw_text_vector(message)


if __name__ == "__main__":
	main()
