from enum import Enum, auto
from dataclasses import dataclass, field
import pygame as py
from random import choice
from pathlib import Path


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
    name: str = ""
    status: str = 'ready'
    image: None = None
    egg: list = field(default_factory=list)
    rect: list = field(default_factory=list)

    def __post_init__(self):
        self.name = self.colour.name.title()
        image_file = Path(f"{self.name.lower()}egg.png")
        if not (image_file.exists() and image_file.is_file()):
            raise ValueError(f'Image file {image_file} does not exist')
        self.image = py.image.load(f"{self.name.lower()}egg.png")
        for _ in range(2):
            self.egg.append(py.transform.scale(self.image, (150, 150)))
            self.rect.append(self.egg[-1].get_rect())
            self.rect[-1].centerx = SCREEN_W // 2
            self.rect[-1].y = -108

    @property
    def again(self):
        return self.rect[1].y == distance

    def __str__(self):
        return f"{self.name} - status: {self.status}, y: {self.rect[-1].y}"

    def animate(self):
        if self.rect[1].y > SCREEN_H:
            self.status = 'ready'
            self.rect[1].y = -108
        elif self.status == 'start':
            self.rect[1].y += speed
        screen.blit(self.egg[1], self.rect[1])


# Function for random egg
def egg_random():
    choices = [egg for egg in eggs if egg.status == 'ready']
    if choices:
        chosen = choice(choices)
        chosen.status = 'start'


# Start pygame library#
py.init()

# Define title of screen#
py.display.set_caption("Colourful Sorting")
# RGB define colour
BLACK = (0, 0, 0)
# Define size of the screen#
SCREEN_W = 1300
SCREEN_H = 650
screen = py.display.set_mode((SCREEN_W, SCREEN_H))
icon = py.image.load("rainbowegg.png")
py.display.set_icon(icon)
# Display background colour
screen.fill(BLACK)

# Egg Load
eggs = [Egg(colour) for colour in Colour]

# variable use for animation
distance = 120
speed = 3
FPS = 80  # variable use for frame rate
clock = py.time.Clock()  # Use the Clock function

# Event detector#
running = True
egg_random()  # pick first egg
while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

    # fill the screen again every time of while running
    screen.fill(BLACK)
    for egg in eggs:
        egg.animate()
        if egg.again:  # room to drop another egg
            egg_random()

    # Update to screen
    py.display.update()
    # Update display for 30 time per second
    clock.tick(FPS)

py.quit()
