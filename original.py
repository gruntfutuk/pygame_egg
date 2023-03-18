import pygame as py
import random

# Start pygame library#
py.init()

# Define title of screen#
py.display.set_caption("Colourful Sorting")
# RGB define colour
Black = (0, 0, 0)
# Define size of the screen#
screen_w = 1300
screen_h = 650
screen = py.display.set_mode((screen_w, screen_h))
icon = py.image.load("rainbowegg.png")
py.display.set_icon(icon)
# Display background colour
screen.fill(Black)

# Egg Load
red_egg = []
red_egg_rect = []
orange_egg = []
orange_egg_rect = []
yellow_egg = []
yellow_egg_rect = []
green_egg = []
green_egg_rect = []
sky_egg = []
sky_egg_rect = []
blue_egg = []
blue_egg_rect = []
purple_egg = []
purple_egg_rect = []

for i in range(2):
    red = py.image.load("redegg.png")
    red_egg.append(py.transform.scale(red, (150, 150)))
    red_egg_rect.append(red_egg[i].get_rect())
    red_egg_rect[i].centerx = screen_w // 2
    red_egg_rect[i].y = -108
    orange = py.image.load("orangeegg.png")
    orange_egg.append(py.transform.scale(orange, (150, 150)))
    orange_egg_rect.append(orange_egg[i].get_rect())
    orange_egg_rect[i].centerx = screen_w // 2
    orange_egg_rect[i].y = -108
    yellow = py.image.load("yellowegg.png")
    yellow_egg.append(py.transform.scale(yellow, (150, 150)))
    yellow_egg_rect.append(yellow_egg[i].get_rect())
    yellow_egg_rect[i].centerx = screen_w // 2
    yellow_egg_rect[i].y = -108
    green = py.image.load("greenegg.png")
    green_egg.append(py.transform.scale(green, (150, 150)))
    green_egg_rect.append(green_egg[i].get_rect())
    green_egg_rect[i].centerx = screen_w // 2
    green_egg_rect[i].y = -108
    sky = py.image.load("skyegg.png")
    sky_egg.append(py.transform.scale(sky, (150, 150)))
    sky_egg_rect.append(sky_egg[i].get_rect())
    sky_egg_rect[i].centerx = screen_w // 2
    sky_egg_rect[i].y = -108
    blue = py.image.load("blueegg.png")
    blue_egg.append(py.transform.scale(blue, (150, 150)))
    blue_egg_rect.append(blue_egg[i].get_rect())
    blue_egg_rect[i].centerx = screen_w // 2
    blue_egg_rect[i].y = -108
    purple = py.image.load("purpleegg.png")
    purple_egg.append(py.transform.scale(purple, (150, 150)))
    purple_egg_rect.append(purple_egg[i].get_rect())
    purple_egg_rect[i].centerx = screen_w // 2
    purple_egg_rect[i].y = -108

# List to random
egg_list = ['red', 'orange', 'yellow', 'green', 'sky', 'blue', 'purple']

# data storage
red_animation = 'ready'
orange_animation = 'ready'
yellow_animation = 'ready'
green_animation = 'ready'
sky_animation = 'ready'
blue_animation = 'ready'
purple_animation = 'ready'


# Function for random egg
def egg_random(dice):
    random_choice = random.choice(dice)
    egg_animation(random_choice)


def egg_check(again, choice):
    global distance
    if again == distance:
        egg_random(choice)

    # Function for animation of egg


def egg_animation(random_choice):
    global screen_w
    global red_animation, orange_animation, yellow_animation, green_animation, sky_animation
    global blue_animation, purple_animation
    if random_choice == 'red':
        red_animation = 'start'
        egg_list.remove('red')
    elif random_choice == 'orange':
        orange_animation = 'start'
        egg_list.remove('orange')
    elif random_choice == 'yellow':
        yellow_animation = 'start'
        egg_list.remove('yellow')
    elif random_choice == 'green':
        green_animation = 'start'
        egg_list.remove('green')
    elif random_choice == 'sky':
        sky_animation = 'start'
        egg_list.remove('sky')
    elif random_choice == 'blue':
        blue_animation = 'start'
        egg_list.remove('blue')
    elif random_choice == 'purple':
        purple_animation = 'start'
        egg_list.remove('purple')


egg_random(egg_list)

# variable use for animation
distance = 120
speed = 3
FPS = 30  # variable use for frame rate
clock = py.time.Clock()  # Use the Clock function
# Event detector#
running = True
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
    # fill the screen again every time of while running
    screen.fill(Black)

    if red_egg_rect[1].y > screen_h:
        red_animation = 'ready'
        egg_list.append('red')
        red_egg_rect[1].y = -108
    elif red_animation == 'start':
        egg_check(red_egg_rect[1].y, egg_list)
        red_egg_rect[1].y += speed
        screen.blit(red_egg[1], red_egg_rect[1])

    if orange_egg_rect[1].y > screen_h:
        orange_animation = 'ready'
        egg_list.append('orange')
        orange_egg_rect[1].y = -108
    elif orange_animation == 'start':
        egg_check(orange_egg_rect[1].y, egg_list)
        orange_egg_rect[1].y += speed
        screen.blit(orange_egg[1], orange_egg_rect[1])

    if yellow_egg_rect[1].y > screen_h:
        yellow_animation = 'ready'
        egg_list.append('yellow')
        yellow_egg_rect[1].y = -108
    elif yellow_animation == 'start':
        egg_check(yellow_egg_rect[1].y, egg_list)
        yellow_egg_rect[1].y += speed
        screen.blit(yellow_egg[1], yellow_egg_rect[1])

    if green_egg_rect[1].y > screen_h:
        green_animation = 'ready'
        egg_list.append('green')
        green_egg_rect[1].y = -108
    elif green_animation == 'start':
        egg_check(green_egg_rect[1].y, egg_list)
        green_egg_rect[1].y += speed
        screen.blit(green_egg[1], green_egg_rect[1])

    if sky_egg_rect[1].y > screen_h:
        sky_animation = 'ready'
        egg_list.append('sky')
        sky_egg_rect[1].y = -108
    elif sky_animation == 'start':
        egg_check(sky_egg_rect[1].y, egg_list)
        sky_egg_rect[1].y += speed
        screen.blit(sky_egg[1], sky_egg_rect[1])

    if blue_egg_rect[1].y > screen_h:
        ble_animation = 'ready'
        egg_list.append('blue')
        blue_egg_rect[1].y = -108
    elif blue_animation == 'start':
        egg_check(blue_egg_rect[1].y, egg_list)
        blue_egg_rect[1].y += speed
        screen.blit(blue_egg[1], blue_egg_rect[1])

    if purple_egg_rect[1].y > screen_h:
        purple_animation = 'ready'
        egg_list.append('purple')
        purple_egg_rect[1].y = -108
    elif purple_animation == 'start':
        egg_check(purple_egg_rect[1].y, egg_list)
        purple_egg_rect[1].y += speed
        screen.blit(purple_egg[1], purple_egg_rect[1])

    # Update to screen
    py.display.update()
    # Update display for 30 time per second
    clock.tick(FPS)
py.quit()
