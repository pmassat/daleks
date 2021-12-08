# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 14:26:16 2021

@author: Pierre
"""

# Import the Turtle Graphics and random modules
import turtle
import random

# Define program constants
nhsquares = 24# number of horizontal squares
nvsquares = 24
WIDTH = (nhsquares+1)*20
HEIGHT = (nvsquares+1)*20
DELAY = 100  # Milliseconds
CHAR_SIZE = 20

offsets = {
    "north": (0, 20),
    "south": (0, -20),
    "west": (-20, 0),
    "east": (20, 0),
    "northeast": (20, 20),
    "northwest": (-20, 20),
    "southeast": (20, -20),
    "southwest": (-20, -20)
}


def bind_direction_keys():
    for key in ["Up", "8"]:
        screen.onkey(lambda: move_drwho("north"), key)
    for key in ["Down", "2"]:
        screen.onkey(lambda: move_drwho("south"), key)
    for key in ["Left", "4"]:
        screen.onkey(lambda: move_drwho("west"), key)
    for key in ["Right", "6"]:
        screen.onkey(lambda: move_drwho("east"), key)
    screen.onkey(lambda: move_drwho("northeast"), "9")
    screen.onkey(lambda: move_drwho("northwest"), "7")
    screen.onkey(lambda: move_drwho("southeast"), "3")
    screen.onkey(lambda: move_drwho("southwest"), "1")


def move_drwho(direction):
    drwho.clearstamps()  # Remove existing stamps made by drwho.
    new_drwho_pos = tuple(x1 + x2 for x1, x2 in zip(drwho.pos(), offsets[direction]))
    drwho.goto(new_drwho_pos)
    drwho.stamp()

# def game_loop():
#     drwho.clearstamps()  # Remove existing stamps made by drwho.

#     new_head = snake[-1].copy()
#     new_head[0] += offsets[snake_direction][0]
#     new_head[1] += offsets[snake_direction][1]

#     # Check collisions
#     if new_head in snake or new_head[0] < - WIDTH / 2 or new_head[0] > WIDTH / 2 \
#             or new_head[1] < - HEIGHT / 2 or new_head[1] > HEIGHT / 2:
#         reset()
#     else:
#         # Add new head to snake body.
#         snake.append(new_head)

#         # Check dalek collision
#         if not food_collision():
#             snake.pop(0)  # Keep the snake the same length unless fed.

#         # Draw snake for the first time.
#         for segment in snake:
#             drwho.goto(segment[0], segment[1])
#             drwho.stamp()

#         # Refresh screen
#         screen.title(f"Dalek Game. Score: {score}")
#         screen.update()

#         # # Rinse and repeat
#         # turtle.ontimer(game_loop, DELAY)


# def food_collision():
#     global dalek_pos, score
#     if get_distance(snake[-1], dalek_pos) < 20:
#         score += 1  # score = score + 1
#         dalek_pos = get_random_dalek_pos()
#         dalek.goto(dalek_pos)
#         return True
#     return False


def get_random_drwho_pos():
    x = random.randint(- nhsquares / 3, nhsquares / 3)*20
    y = random.randint(- nvsquares / 3, nvsquares / 3)*20
    return (x, y)


def get_random_dalek_pos():
    x = random.randint(- nhsquares / 2 + 1, nhsquares / 2 - 1)*20
    y = random.randint(- nvsquares / 2 + 1, nvsquares / 2 - 1)*20
    return (x, y)

# def get_distance(pos1, pos2):
#     x1, y1 = pos1
#     x2, y2 = pos2
#     distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5  # Pythagoras' Theorem
#     return distance


def reset():
    global score, snake, snake_direction, dalek_pos
    score = 0
    xdr, ydr = drwho.pos()
    for dalek in daleks:
        dalek_pos = get_random_dalek_pos()
        x, y = dalek_pos
        while abs(xdr-x)<CHAR_SIZE or abs(ydr-y)<CHAR_SIZE:
            dalek_pos = get_random_dalek_pos()
            x, y = dalek_pos
        dalek.goto(dalek_pos)
        dalek.stamp()
    # game_loop()


# Create a window where we will do our drawing.
screen = turtle.Screen()
screen.setup(WIDTH, HEIGHT)  # Set the dimensions of the Turtle Graphics window.
screen.title("Daleks")
screen.bgcolor("beige")
screen.tracer(0)  # Turn off automatic animation.

# Event handlers
screen.listen()
bind_direction_keys()
screen.onkey(turtle.bye, "Escape")

# Create a turtle to do your bidding
drwho = turtle.Turtle()
drwho.shape("turtle")
# drwho.color('red')
# drwho.penup()
drwho_pos = get_random_dalek_pos()
drwho.goto(drwho_pos)
drwho.stamp()

# dalek
num_dalek = 6
daleks = []
for nd in range(num_dalek):
    dalek = turtle.Turtle()
    dalek.shape("circle")
    dalek.color("red")
    dalek.shapesize(CHAR_SIZE / 20)
    dalek.penup()
    daleks.append(dalek)

# Set animation in motion
reset()

# Finish nicely
turtle.done()
