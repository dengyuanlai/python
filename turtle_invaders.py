import random
import time
import turtle

FPS = 30
FRAME_MS = int(1000 / FPS)

CANNON_STEP = 10
LASER_LENGTH = 10
LASER_SPEED = 20
ALIEN_SPAWN_INTERVAL = 4  # Seconds
ALIEN_SPEED = 1

window = None
LEFT = 0.0
RIGHT = 0.0
TOP = 0.0
BOTTOM = 0.0
FLOOR_LEVEL = 0.0
GUTTER = 0.0

cannon = None
text = None
lasers = []
aliens = []

def draw_cannon():
    cannon.clear()
    cannon.turtlesize(1, 4)  # Base
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 10)
    cannon.turtlesize(1, 1.5)  # Next tier
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL + 20)
    cannon.turtlesize(0.8, 0.3)  # Tip of cannon
    cannon.stamp()
    cannon.sety(FLOOR_LEVEL)


def move_left():
    cannon.cannon_movement = -1


def move_right():
    cannon.cannon_movement = 1


def stop_cannon_movement():
    cannon.cannon_movement = 0


def create_laser():
    laser = turtle.Turtle()
    laser.penup()
    laser.color(1, 0, 0)
    laser.hideturtle()
    laser.setposition(cannon.xcor(), cannon.ycor())
    laser.setheading(90)
    # Move laser to just above cannon tip
    laser.forward(20)
    # Prepare to draw the laser
    laser.pendown()
    laser.pensize(5)

    lasers.append(laser)


def move_laser(laser):
    laser.clear()
    laser.forward(LASER_SPEED)
    # Draw the laser
    laser.forward(LASER_LENGTH)
    laser.forward(-LASER_LENGTH)


def create_alien():
    alien = turtle.Turtle()
    alien.penup()
    alien.turtlesize(1.5)
    alien.setposition(
        random.randint(
            int(LEFT + GUTTER),
            int(RIGHT - GUTTER),
        ),
        TOP,
    )
    alien.shape("turtle")
    alien.setheading(-90)
    alien.color(random.random(), random.random(), random.random())
    aliens.append(alien)


def remove_sprite(sprite, sprite_list):
    sprite.clear()
    sprite.penup()
    sprite.hideturtle()
    sprite.setposition(RIGHT + 1000, TOP + 1000)
    if sprite in sprite_list:
        sprite_list.remove(sprite)


alien_timer = 0.0
game_timer = 0.0
score = 0
game_running = False


def setup_window():
    global window, LEFT, RIGHT, TOP, BOTTOM, FLOOR_LEVEL, GUTTER

    window = turtle.Screen()
    window.tracer(0)
    window.setup(0.5, 0.75)
    window.bgcolor(0.2, 0.2, 0.2)
    window.title("The Real Python Space Invaders")

    LEFT = -window.window_width() / 2
    RIGHT = window.window_width() / 2
    TOP = window.window_height() / 2
    BOTTOM = -window.window_height() / 2
    FLOOR_LEVEL = 0.9 * BOTTOM
    GUTTER = 0.025 * window.window_width()


def setup_cannon():
    global cannon

    cannon = turtle.Turtle()
    cannon.penup()
    cannon.color(1, 1, 1)
    cannon.shape("square")
    cannon.setposition(0, FLOOR_LEVEL)
    cannon.cannon_movement = 0  # -1, 0 or 1 for left, stationary, right


def setup_text():
    global text

    text = turtle.Turtle()
    text.penup()
    text.hideturtle()
    text.setposition(LEFT * 0.8, TOP * 0.8)
    text.color(1, 1, 1)


def bind_keys():
    window.onkeypress(move_left, "Left")
    window.onkeypress(move_right, "Right")
    window.onkeyrelease(stop_cannon_movement, "Left")
    window.onkeyrelease(stop_cannon_movement, "Right")
    window.onkeypress(create_laser, "space")
    window.onkeypress(turtle.bye, "q")
    window.listen()


def initialize_game_state():
    global lasers, aliens, alien_timer, game_timer, score, game_running

    lasers = []
    aliens = []
    alien_timer = time.monotonic()
    game_timer = time.monotonic()
    score = 0
    game_running = True


def setup_game():
    setup_window()
    setup_cannon()
    setup_text()
    bind_keys()
    draw_cannon()
    initialize_game_state()


def end_game():
    splash_text = turtle.Turtle()
    splash_text.hideturtle()
    splash_text.color(1, 1, 1)
    splash_text.write("GAME OVER", font=("Courier", 40, "bold"), align="center")
    window.update()


def update_hud(now):
    time_elapsed = now - game_timer
    text.clear()
    text.write(
        f"Time: {time_elapsed:5.1f}s\nScore: {score:5}",
        font=("Courier", 20, "bold"),
    )


def update_cannon_position():
    new_x = cannon.xcor() + CANNON_STEP * cannon.cannon_movement
    if LEFT + GUTTER <= new_x <= RIGHT - GUTTER:
        cannon.setx(new_x)
        draw_cannon()


def update_lasers_and_collisions():
    global score

    for laser in lasers.copy():
        move_laser(laser)
        # Remove laser if it goes off screen
        if laser.ycor() > TOP:
            remove_sprite(laser, lasers)
            continue

        # Check for collision with aliens
        hit_alien = None
        for alien in aliens.copy():
            if laser.distance(alien) < 20:
                hit_alien = alien
                break

        if hit_alien is not None:
            remove_sprite(laser, lasers)
            remove_sprite(hit_alien, aliens)
            score += 1


def spawn_aliens(now):
    global alien_timer

    if now - alien_timer > ALIEN_SPAWN_INTERVAL:
        create_alien()
        alien_timer = now


def move_aliens():
    for alien in aliens:
        alien.forward(ALIEN_SPEED)
        # Check for game over
        if alien.ycor() < FLOOR_LEVEL:
            return True
    return False


def tick():
    global game_running

    if not game_running:
        return

    now = time.monotonic()
    update_hud(now)
    update_cannon_position()
    update_lasers_and_collisions()
    spawn_aliens(now)

    if move_aliens():
        game_running = False
        end_game()

    window.update()
    if game_running:
        window.ontimer(tick, FRAME_MS)


def main():
    setup_game()
    tick()
    turtle.done()


if __name__ == "__main__":
    main()
