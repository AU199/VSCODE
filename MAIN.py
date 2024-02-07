import pygame
import math

pygame.init()

WIDTH= 1020
HEIGHT = 900
seconds = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))

rectangle_thing = []

class ball:
    def __init__(self, x, y,v_speed, h_speed, cof_of_restitution, ball_num,gravitiy_constant, color, stop):
        self.y = y
        self.stop = stop
        self.x = x
        self.v_speed = v_speed
        self.h_speed = h_speed
        self.starting_height = y
        self.bounces_num = 0
        self.nums_bounces = 1
        self.cof_of_restitution = cof_of_restitution
        self.predicted_height = 0
        self.ball_num = ball_num
        self.predicted_height = (self.cof_of_restitution**2)*self.starting_height
        self.color = color
        self.gravitiy_constant = gravitiy_constant
        self.path = []
        self.slope = 0

    def gravity(self):
        if self.y < self.stop or self.bounces_num != 0:

                if self.bounces_num == 0:
                    self.v_speed += ((self.gravitiy_constant*2)/(int(((self.y))*-1)**2))*2
                  
                    self.y += self.v_speed
                    self.x += self.h_speed
                else:
                    self.v_speed += ((self.gravitiy_constant*2)/(int(((self.y))*-1)**2))*2
                    self.y += self.v_speed
                    self.x += self.h_speed
                    if self.v_speed > 0:
                        self.bounces_num = 0
                        if self.predicted_height != 0 and self.y < 499:
                            print(f"the current starting height {self.starting_height} and predicted height of ball number {self.ball_num} is {self.predicted_height} and the deviation from actual is {self.predicted_height-self.starting_height}")
                        self.starting_height = self.y
                        self.predicted_height = (self.cof_of_restitution**2)*self.predicted_height
                self.path.append((self.x,self.y))





        elif self.bounces_num == 0:
            self.bounces_num = 1
            self.v_speed = ((self.v_speed))*-1*self.cof_of_restitution
            self.h_speed = self.h_speed *self.cof_of_restitution
            # if self.h_speed != 0 or self.v_speed <-1.8092307692307694e-05:
            #     print(f"the current vertical speed is {self.v_speed}, and horizontal speed {self.h_speed} of ball number {self.ball_num}")
            self.nums_bounces += 1
            self.path.append((self.x,self.y))


    def cal_slope(self):
        print(len(self.path))
        if len(self.path) > 1:
            list_thing = self.path[len(self.path)-2]
            print(self.x,self.y)
            print(list_thing)
            if self.x > list_thing[0]:
                print()
                self.slope = ((self.y-list_thing[1])/(self.x - list_thing[0]))*-1
        print("slope", self.slope, "of ball", self.ball_num)

    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),5)
        for i in range(len(self.path)):
            pygame.draw.circle(screen,(30,240,200),self.path[i],3)


ball_1 = ball(y = 100, x =20, v_speed= 0 , h_speed= 0.15 , cof_of_restitution= 0.3 , ball_num= 1 , gravitiy_constant= 9.8, color = (200,200,0),stop=700)
ball_2 = ball(y = 100, x =40, v_speed= 0.6 , h_speed= 0.15 , cof_of_restitution= 0.3 , ball_num= 2 , gravitiy_constant= 9.8, color = (0,255,0),stop=700)
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            new_rect = pygame.Rect(mouse_x, mouse_y, 50, 30)
            rectangle_thing.append(new_rect)
    seconds += 0.1
    ball_1.cal_slope()
    ball_1.gravity()
    ball_1.draw()
    ball_2.gravity()
    ball_2.draw()
    for i in range(len(rectangle_thing)):
        pygame.draw.rect(screen,(233,0,0),rectangle_thing[i])
    pygame.display.flip()