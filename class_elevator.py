from settings import *

class elevator:

    def __init__(self, elevator_id):
        self.elevator_id = elevator_id
        self.current = 0
        self.order = {}
        # key - num_floor, value - time 
        #self.moving = moving

    def calc_time(self, current):
        if not self.order:
            return abs(self.current - current) * SPEED_ELEVATOR
        last_order = list(self.order.keys())[-1]
        return abs(current - last_order) * SPEED_ELEVATOR + self.order[last_order] + STOP_ELEVATOR
                      
    def draw_elev(self, screen, x, y):
        img = pygame.image.load('elv.png')
        scaled_image = pygame.transform.scale(img, (ELE_WIGTH, ELE_HEIGHT))
        screen.blit(scaled_image, (x, y))
        pygame.display.flip()
        