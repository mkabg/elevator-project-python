import pygame

SPEED_ELEVATOR = 0.5
STOP_ELEVATOR = 2

WINDOW_WIGTH = 750
WINDOW_HEIGHT = 750

NUM_FLOORS = 15
NUM_ELEVATOR = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 255, 0)
# height floor
IMG_WIGTH = 100
if WINDOW_HEIGHT/50 > NUM_FLOORS:
    IMG_HEIGHT = 50
else:
    IMG_HEIGHT = WINDOW_HEIGHT/NUM_FLOORS

#elevator
ELE_HEIGHT = 50
if WINDOW_WIGTH / 50 > NUM_ELEVATOR:
    ELE_WIGTH = 50
else:
    ELE_WIGTH = (WINDOW_WIGTH - IMG_WIGTH) / NUM_ELEVATOR

#FONT_BUTTON = pygame.font.Font(None, 30)

