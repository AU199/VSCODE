import numpy as np 
import pygame 
import math

def find_angle(slope, intersection_point, v_v):
    print("slope",slope)
    vertical_vector = 1.1
    intersectionpoint = intersection_point

    main_vector = [1, vertical_vector]
    plat_vector = [1,slope]

    lenght_of_m_vector = np.sqrt((1**2+(vertical_vector**2)))
    print(lenght_of_m_vector)
    lenght_of_p_vector = np.sqrt((1**2+(slope**2)))



    dot_product = (np.dot(main_vector,plat_vector))/(lenght_of_m_vector*lenght_of_p_vector)
    print(dot_product)
    result = np.arccos(dot_product)
    print("result", result)
    return result

pygame.init()

# dependencies for the slider code to work
WIDTH,HEIGHT = 900,500
SLIDER_X, SLIDER_Y, SLIDER_WIDTH, SLIDER_HEIGHT = 10, 10, WIDTH - 300, 20
D_SLIDER_X, D_SLIDER_Y, D_SLIDER_WIDTH, D_SLIDER_HEIGHT = 10, 40, WIDTH - 300, 20
#Points
point_one = (300,300)
point_two = (600,300)

screen = pygame.display.set_mode((WIDTH,HEIGHT))


WHITE,RED,BLACK = (233,233,233),(233,0,0),(0,0,0)

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
        slope = (((ep[1]-sp[1]))/((ep[0]-sp[0])))


    curr_pos = first_point
    x = curr_pos[0]
    y = curr_pos[1]
    for i in range(1000):
        x = ((1- ((i+1)/1000))*curr_pos[0]) + second_point[0]*((i+1)/1000)
        if slope != 0:
             y = ((1- ((i+1)/1000))*sp[1]) + ep[1]*((i+1)/1000)
        else:
            y = 0

        g.append((x,y))

    return g,slope
def draw_all_points(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, (233,0,0), points[i],5)
def create_points(point_one,point_two):
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

a = create_points(point_one=point_one,point_two=point_two)
point_list = a
while True:
    point_list = None
    screen.fill(BLACK)

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
    if angle ==0: angle = 0.01
    g = create_points(point_one=point_one,point_two=point_two)
    point_list = g[0]
    slope = g[1]

    find_angle(slope,(2.4,300),3.4)
    draw_slider_angle()
    draw_slider_distance()
    draw_all_points(point_list)

    point_one, point_two = change_angle(point_one,point_two)

    pygame.display.flip()