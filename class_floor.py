from settings import *
import class_button  

class floor:
    def __init__(self, floor_number, button, location_x, location_y):
        self.floor_number = floor_number
        self.button = button
        self.location_x = location_x
        self.location_y = location_y

    def draw_floor(self, screen, x, y):
        img_floor = pygame.image.load("floor.png")
        scaled_image = pygame.transform.scale(img_floor, (IMG_WIGTH, IMG_HEIGHT))
        screen.blit(scaled_image, (x, y))
        pygame.display.flip()

        