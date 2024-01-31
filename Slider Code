import pygame 
import math

pygame.init()

WIDTH,HEIGHT = 900,500
SLIDER_X, SLIDER_Y, SLIDER_WIDTH, SLIDER_HEIGHT = 10, 10, WIDTH - 300, 20
D_SLIDER_X, D_SLIDER_Y, D_SLIDER_WIDTH, D_SLIDER_HEIGHT = 10, 40, WIDTH - 300, 20
#Points
point_one = (300,300)
point_two = (600,300)

screen = pygame.display.set_mode((WIDTH,HEIGHT))

WHITE,RED,BLACK = (233,233,233),(233,0,0),(0,0,0)

angle = 0.1
ANGLE_MAX = 1.56
ANGLE_MIN = -1.56
DISTANCE_MIN = 3
DISTANCE_MAX = 200
distance = 60
slider_pressed = False
distance_slider_pressed = False
point_list = []

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

    slope = ep[0]

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

    return g
def draw_all_points(points):
    for i in range(len(points)):
        pygame.draw.circle(screen, (233,0,0), points[i],5)
def create_points():
    point_list.clear()
    a = car_calc(point_one,point_two)
    return list(a)

def change_angle(point1,point2):
    x1,y1 = point1[0],point1[1]
    x2,y2 = point2[0],point2[1]

    x1 = 600+(math.sin(angle)*distance)
    x2 = 600-(math.sin(angle)*distance)
    y1 = 300+(math.cos(angle)*distance)
    y2 = 300-(math.cos(angle)*distance)

    point_one = (x1,y1)
    point_two = (x2,y2)
    print(point_two,point_one)
    return point_one, point_two

a = create_points()
point_list = a
while True:
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
            print("this is going to the angle")
            mouseX = max(SLIDER_X, min(SLIDER_X + SLIDER_WIDTH, mouseX))
            angle = max(ANGLE_MIN, min(ANGLE_MAX, (mouseX - SLIDER_X) / SLIDER_WIDTH * (ANGLE_MAX - ANGLE_MIN) + ANGLE_MIN))
        if event.type == pygame.MOUSEMOTION and distance_slider_pressed:
            mouseX, mouseY = pygame.mouse.get_pos()
            print("this is going to the distance with distance being ", distance)
            mouseX =max(D_SLIDER_X, min(D_SLIDER_X + D_SLIDER_WIDTH, mouseX))
            distance = max(DISTANCE_MIN, min(DISTANCE_MAX, (mouseX - D_SLIDER_X) / D_SLIDER_WIDTH * (DISTANCE_MAX - DISTANCE_MIN) + DISTANCE_MIN))


    draw_slider_angle()
    draw_slider_distance()
    draw_all_points(point_list)
    print("creating points")
    point_list = create_points()
    point_one, point_two = change_angle(point_one,point_two)
    print(f"point one {point_one}, point two {point_two}")

    pygame.display.flip()