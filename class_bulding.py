from class_floor import floor
from class_button import Button
from class_elevator import elevator
from collections import OrderedDict
from settings import *



class building:
    def __init__(self, num_floors, num_elevators):
        self.num_floors = num_floors
        self.num_elevators = num_elevators

    def calc_min_time(self):
        pass

    def draw(self):
        pygame.init() 
        screen = pygame.display.set_mode((WINDOW_WIGTH, WINDOW_HEIGHT)) 
        screen.fill(WHITE) 
        floors = []
        elevators = []
        order = OrderedDict()
         
        FONT_BUTTON = pygame.font.Font(None, 30)
        # x = 0
        # y = WINDOW_WIGTH - IMG_HEIGHT
        location_x = x = 0
        location_y = y = WINDOW_WIGTH - IMG_HEIGHT
        for num_floor in range(self.num_floors):
            b = Button(x, y + 15, 25, IMG_HEIGHT - 20, str(num_floor), FONT_BUTTON, GRAY, DARK_GRAY, BLACK)
            floors.append(floor(num_floor, b, location_x, location_y))
            floors[-1].draw_floor(screen, x, y)
            y -= IMG_HEIGHT
       
        x = IMG_WIGTH
        y = WINDOW_WIGTH - IMG_HEIGHT
        for elevator_id in range(self.num_elevators):
            elevators.append(elevator(elevator_id))
            elevators[-1].draw_elev(screen, x, y)
            x += ELE_WIGTH

    

        run = True
        while run:
            for c_floor in floors:
                c_floor.button.draw(screen)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                for c_floor in floors:
                    if c_floor.button.is_clicked(event):
                        c_floor.button.change_color(GREEN)
                        # n_f_o = int(c_floor.button.text)
                        # t_e = []
                        # for elevator_id in elevators:
                        #     time_elev = elevator_id.calc_time(current = c_floor)
                        #     t_e.append(time_elev)
                        # order.update({n_f_o : min(time_elev)})
                            
            pygame.display.flip()
            pygame.display.update()
        pygame.quit()

#main
build = building(NUM_FLOORS, NUM_ELEVATOR)
build.draw() 

