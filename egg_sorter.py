from enum import Enum, auto
from dataclasses import dataclass, field
import pygame as py
from random import choice
import logging
from time import sleep

class Colour(Enum):
    RED = auto()
    ORANGE = auto()
    YELLOW = auto()
    GREEN = auto()
    SKY = auto()
    BLUE = auto()
    PURPLE = auto()

@dataclass
class Egg:
    colour: Colour
    status: str = 'ready'
    image: None = None
    egg: list = field(default_factory=list)
    rect: list = field(default_factory=list)

    def __post_init__(self):
        self.image = py.image.load(f"{self.name.lower()}egg.png")
        for _ in range(2):
            self.egg.append(py.transform.scale(self.image, (150, 150)))
            self.rect.append(self.egg[-1].get_rect())
            self.rect[-1].centerx = screen_w // 2
            self.rect[-1].y = -108

    @property
    def name(self):
        return self.colour.name

    @property
    def again(self):
        return self.rect[1].y == distance

    def __str__(self):
        return (
                f"{self.name} - status: {self.status}, y: {self.rect[-1].y}"
                )

    def animate(self):
        if self.rect[1].y > screen_h:
            self.status = 'ready'
            self.rect[1].y = -108
            screen.blit(self.egg[1], self.rect[1])
            logging.info(f'animate reset: {self}')
        elif self.status == 'start':
            self.rect[1].y += speed
            screen.blit(self.egg[1], self.rect[1])
            logging.info(f'animate moved down: {self}')


# Function for random egg
def egg_random():
    choices = [egg for egg in eggs if egg.status == 'ready']
    logging.info(f'Choices: {", ".join(egg.name for egg in choices)}')
    if choices:
        chosen = choice(choices)
        chosen.status = 'start'
        logging.info(f'Picked: {chosen.name}')


# set up logging
logging.basicConfig(level=logging.CRITICAL, format='** DEBUGGING ** %(message)s')

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
eggs = [Egg(colour) for colour in Colour]

# variable use for animation
distance = 120
speed = 3
FPS = 30  # variable use for frame rate
clock = py.time.Clock()  # Use the Clock function

# Event detector#
running = True
egg_random()  # pick first egg
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen again every time of while running
    screen.fill(Black)
    for egg in eggs:
        egg.animate()
        if egg.again:  # room to drop another egg
            logging.info(f'distance check: {egg.rect[1].y == distance} ({distance})')
            egg_random()

    # Update to screen
    py.display.update()
    # Update display for 30 time per second
    clock.tick(FPS)
py.quit()
