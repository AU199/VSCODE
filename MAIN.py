import pygame
import math
import numpy as np
import sys
import os

pygame.init()

WIDTH= 1020
HEIGHT = 900
seconds = 0
screen = pygame.display.set_mode((WIDTH,HEIGHT))
SLIDER_X, SLIDER_Y, SLIDER_WIDTH, SLIDER_HEIGHT = 10, 10, WIDTH - 300, 20
D_SLIDER_X, D_SLIDER_Y, D_SLIDER_WIDTH, D_SLIDER_HEIGHT = 10, 40, WIDTH - 300, 20
#Points
point_one = (300,300)
point_two = (600,300)

screen = pygame.display.set_mode((WIDTH,HEIGHT))


WHITE,RED,BLACK = (233,233,233),(233,0,0),(0,0,0)
epsilon = sys.float_info.epsilon+1

angle = 0.1
ANGLE_MAX =1.5707963270658885
ANGLE_MIN = -1.5707963270658885
DISTANCE_MIN = 3
DISTANCE_MAX = 200
distance = 60
slider_pressed = False
distance_slider_pressed = False
point_list = None
slope = None
rectangle_thing = []
point_list = []
all_points = []
r_angles = []
last_lenght_points = 0
p_slope = []


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
        self.cof_of_restitution = cof_of_restitution # this is the coefficent of restetution
        self.predicted_height = 0
        self.ball_num = ball_num
        self.predicted_height = (self.cof_of_restitution**2)*self.starting_height
        self.color = color
        self.gravitiy_constant = gravitiy_constant
        self.path = []
        self.slope = 0
        self.hitting = 0

    def gravity(self):
        if self.y < self.stop or self.bounces_num != 0 and self.hitting == 0:
                # this simulates the gravity constant that is given in self.gravity
                self.v_speed += ((self.gravitiy_constant*2)/(int(((self.y))*-1)**2))*2
                self.y += self.v_speed
                self.x += self.h_speed
                self.path.append((self.x,self.y))
       


        elif self.bounces_num == 0:
            self.bounces_num = 1
            #sets speed to negative of itself, and multiplies it based on the coefficient of restitution 
            self.v_speed = ((self.v_speed))*-1*self.cof_of_restitution
            #changes the horizontal speed to half of itself
            self.h_speed = self.h_speed * 0.5
            # if self.h_speed != 0 or self.v_speed <-1.8092307692307694e-05:
            #     print(f"the current vertical speed is {self.v_speed}, and horizontal speed {self.h_speed} of ball number {self.ball_num}")
            self.nums_bounces += 1
            self.path.append((self.x,self.y))
        if self.hitting == 1:
            self.hitting = 0
            print("horizontal speed", self.h_speed*-1,"vertical speed", self.v_speed*-1)
            print("new y", self.y + self.v_speed*-1, "new x", self.x + self.h_speed*-1)

            self.h_speed = self.h_speed*-1.5
            self.v_speed = self.v_speed*-1.5




    def cal_slope(self):
        if len(self.path) > 1:
            list_thing = self.path[len(self.path)-2]
            if self.x > list_thing[0]:
                self.slope = ((self.y-list_thing[1])/(self.x - list_thing[0]))*-1
        for i in range(-5,5,1):
            if i < 0:
                new_x_y = (self.x+i,self.y-(self.slope*i))
            if i > 0:
                new_x_y = (self.x+i,self.y+(self.slope*i)*-1)
            if i ==0:
                new_x_y = (self.x,self.y)
            pygame.draw.circle(screen,(255,0,0),new_x_y,4)

    def draw(self):

        pygame.draw.circle(screen,self.color,(self.x,self.y),5)
        # for i in range(len(self.path)):
        #     pygame.draw.circle(screen,(30,240,200),self.path[i],3)

    def check_if(self):
        distance_list = []
        for item in point_list:
            x,y = item
            x2 = self.x
            y2 = self.y
            distance = math.sqrt((x2-x)**2+(y2-y)**2)
            distance_list.append(distance)

        for distance in distance_list:
            if distance<8:
                    self.hitting = 1

            

def find_angle(slope):
    vertical_vector = 3.4
    intersectionpoint = (2.4,300)

    main_vector = [1, vertical_vector]
    plat_vector = [1,slope]

    lenght_of_m_vector = np.sqrt((1**2+(vertical_vector**2)))
    lenght_of_p_vector = np.sqrt((1**2+(slope**2)))



    dot_product = (np.dot(main_vector,plat_vector))/(lenght_of_m_vector*lenght_of_p_vector)
    result = np.arccos(dot_product)

def draw_slider_angle():
    pygame.draw.rect(screen, WHITE, (SLIDER_X, SLIDER_Y, SLIDER_WIDTH, SLIDER_HEIGHT))
    slider_pos = (angle - ANGLE_MIN) / (ANGLE_MAX - ANGLE_MIN) * SLIDER_WIDTH + SLIDER_X
    pygame.draw.rect(screen, RED, (slider_pos - 5, SLIDER_Y - 5, 10, SLIDER_HEIGHT + 10))
def draw_slider_distance():
    pygame.draw.rect(screen, WHITE,(D_SLIDER_X,D_SLIDER_Y,D_SLIDER_WIDTH,D_SLIDER_HEIGHT))
    slider_pos = (distance - DISTANCE_MIN) / (DISTANCE_MAX - DISTANCE_MIN) * D_SLIDER_WIDTH + D_SLIDER_X
    pygame.draw.rect(screen,RED,(slider_pos - 5, D_SLIDER_Y - 5, 10, D_SLIDER_HEIGHT + 10))

def car_calc(first_point, second_point):
    ep = first_point
    sp = second_point
    move = (sp[0]-ep[0])*-1
    rise = (sp[1]-ep[1])*-1
    g = []

    if move != 0:
        slope = (((ep[1]-sp[1])*-1)/((ep[0]-sp[0])*-1))


    curr_pos = first_point
    x = curr_pos[0]
    y = curr_pos[1]
    for i in range(10000):
        x = ((1- ((i+1)/10000))*curr_pos[0]) + second_point[0]*((i+1)/10000)
        if slope != 0:
             y = ((1- ((i+1)/10000))*sp[1]) + ep[1]*((i+1)/10000)
        else:
            y = 0

        g.append((x,y))

    return g,slope

def draw_all_points(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, (233,0,0), points[i],5)

def create_points():
    a = car_calc(point_one,point_two)
    return list(a[0]), a[1]

def change_angle(point1,point2):
    x1,y1 = point1[0],point1[1]
    x2,y2 = point2[0],point2[1]

    x1 = 600+(math.sin(angle)*distance)
    x2 = 600-(math.sin(angle)*distance)
    y1 = 300+(math.cos(angle)*distance)
    y2 = 300-(math.cos(angle)*distance)

    point_one = (x1,y1)
    point_two = (x2,y2)
    return point_one, point_two

def slope_p(point_list):
    p_list = point_list
    p_slope = []
    
    if len(p_list) > 1:
        for i in range(0,int(len(p_list)/10000)-1,10000):
            ep = p_list[i+10000]
            sp = p_list[i]
            move = (sp[0]-ep[0])*-1
            rise = (sp[1]-ep[1])*-1
            if move != 0:
                slope = ((ep[1]-sp[1]))/((ep[0]-sp[0]))
                p_slope.append(slope)
            



ball_1 = ball(y = 100, x =20, v_speed= 0 , h_speed= 0.15 , cof_of_restitution= 0.3 , ball_num= 1 , gravitiy_constant= 9.8, color = (200,200,0),stop=900)
# ball_3 = ball(x=0,y=900,v_speed = -4, h_speed= 0.4, cof_of_restitution= 0.4, ball_num= 3, gravitiy_constant= 9.8, color= (0,0,255),stop= 900)
#ball_2 = ball(y = 100, x =40, v_speed= 0.6 , h_speed= 0.15 , cof_of_restitution= 0.3 , ball_num= 2 , gravitiy_constant= 9.8, color = (0,255,0),stop=1000)
last_lenght = 0
#Main Loop
while True:
    screen.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX, mouseY = pygame.mouse.get_pos()
            if (
                SLIDER_X <= mouseX <= SLIDER_X + SLIDER_WIDTH
                and SLIDER_Y <= mouseY <= SLIDER_Y + SLIDER_HEIGHT
            ):
                slider_pressed = True
            elif (
                D_SLIDER_X <= mouseX <= D_SLIDER_X + D_SLIDER_WIDTH 
                and D_SLIDER_Y <= mouseY <= D_SLIDER_Y + D_SLIDER_HEIGHT
            ):
                distance_slider_pressed = True
            else:

                point_one = (mouseX,mouseY)
                x2 = mouseX-(math.sin(angle)*distance)
                y2 = mouseY-(math.cos(angle)*distance)
                all_points.append(point_one)
                all_points.append((x2,y2))
        if event.type == pygame.MOUSEBUTTONUP:
            slider_pressed = False
            distance_slider_pressed = False
        
        if event.type == pygame.MOUSEMOTION and slider_pressed:
            mouseX, mouseY = pygame.mouse.get_pos()

            mouseX = max(SLIDER_X, min(SLIDER_X + SLIDER_WIDTH, mouseX))
            angle = max(ANGLE_MIN, min(ANGLE_MAX, (mouseX - SLIDER_X) / SLIDER_WIDTH * (ANGLE_MAX - ANGLE_MIN) + ANGLE_MIN))
        if event.type == pygame.MOUSEMOTION and distance_slider_pressed:
            mouseX, mouseY = pygame.mouse.get_pos()
            mouseX =max(D_SLIDER_X, min(D_SLIDER_X + D_SLIDER_WIDTH, mouseX))
            distance = max(DISTANCE_MIN, min(DISTANCE_MAX, (mouseX - D_SLIDER_X) / D_SLIDER_WIDTH * (DISTANCE_MAX - DISTANCE_MIN) + DISTANCE_MIN))
    seconds += 0.1
    ball_1.cal_slope()
    ball_1.gravity()
    ball_1.draw()
    ball_1.check_if()
    #ball_2.gravity()
    #ball_2.draw()
    # ball_3.gravity()
    # ball_3.draw()
    if len(all_points)>last_lenght:
        last_lenght += 2
        point_list = []
        for i in range(0,len(all_points)-1,2):
            point_one = all_points[i]
            point_two = all_points[i+1]
            g = create_points()
            point_list.extend(g[0])
            slope = g[1]
            find_angle(slope)
    if last_lenght_points <len(point_list):
        last_lenght_points = len(point_list)
        slope_p(point_list = point_list)
    draw_slider_angle()
    draw_slider_distance()
    draw_all_points(point_list)
    for i in range(len(rectangle_thing)):
        pygame.draw.rect(screen,(233,0,0),rectangle_thing[i])
    pygame.display.flip()