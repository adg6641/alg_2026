

import math


print("-- math module --")

print("sqrt(16):", math.sqrt(16))

print("pi:", math.pi)
print()


print("-- degree and radian --")

degree = 90
radian = math.radians(degree)

print("degree:", degree)
print("radian:", radian)
print("sin(90 degrees):", math.sin(radian))
print("back to degree:", math.degrees(radian))
print()


print("-- rotate point --")


def rotate_point(x, y, degree):
    theta = math.radians(degree)
    rotated_x = x * math.cos(theta) - y * math.sin(theta)
    rotated_y = x * math.sin(theta) + y * math.cos(theta)
    return rotated_x, rotated_y


point = (1, 0)
rotated = rotate_point(point[0], point[1], 90)

print("before:", point)
print("after 90 degree rotation:", rotated)
print()


print("-- pygame window demo is prepared below --")


RUN_PYGAME_DEMO = False


def run_pygame_window():
    import pygame as pg

    pg.init()
    screen = pg.display.set_mode((640, 480))
    pg.display.set_caption("Python Module Demo")

    demo_points = [(-120, -60), (0, 0), (120, 80)]

    def to_screen(x, y):
        width, height = screen.get_size()
        center_x = width // 2
        center_y = height // 2
        return center_x + x, center_y - y

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        screen.fill((250, 250, 250))

        width, height = screen.get_size()
        center_x = width // 2
        center_y = height // 2

        pg.draw.line(screen, (180, 180, 180), (0, center_y), (width, center_y), 1)
        pg.draw.line(screen, (180, 180, 180), (center_x, 0), (center_x, height), 1)

        for x, y in demo_points:
            pg.draw.circle(screen, (37, 99, 235), to_screen(x, y), 6)

        for i in range(len(demo_points) - 1):
            start = to_screen(demo_points[i][0], demo_points[i][1])
            end = to_screen(demo_points[i + 1][0], demo_points[i + 1][1])
            pg.draw.line(screen, (217, 119, 6), start, end, 3)

        pg.display.flip()

    pg.quit()


if RUN_PYGAME_DEMO:
    run_pygame_window()
