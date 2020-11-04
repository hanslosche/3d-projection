import pygame
import os
import math

from matrix import matrix_multiplication
os.environ["SDL_VIDEO_CENTERED"]='1'
width, height = 860, 720
black, white, blue = (20, 20, 20), (230, 230, 230), (0,154, 255)

# pygame configurations
pygame.init()
pygame.display.set_caption("3D cube Projection")
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fps = 60

angle = 0
cube_position = [width//2, height//2]
scale = 600
speed = 0.01

points = [n for n in range(8)]

points[0] = [[-1], [-1], [1]]
points[1] = [[1], [-1], [1]]
points[2] = [[1], [1], [1]]
points[3] = [[-1], [1], [1]]
points[4] = [[-1], [-1], [-1]]
points[5] = [[1], [-1], [-1]]
points[6] = [[1], [1], [-1]]
points[7] = [[-1], [1], [-1]]
def connect_points(i, j, k):
    a = k[i]
    b = k[j]
    pygame.draw.line(screen, black, (a[0], a[1]), (b[0], b[1]), 2)


run = True
while run:
    clock.tick(fps)
    screen.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    index = 0

    projected_points = [j for j in range(len(points))]

    rotation_x = [[1, 0, 0],
                 [0, math.cos(angle), -math.sin(angle)],
                 [0, math.sin(angle), math.cos(angle)]]

    rotation_y = [[math.cos(angle), 0, -math.sin(angle)],
                [0, 1, 0],
                 [math.sin(angle), 0, math.cos(angle)]]

    rotation_z = [[math.cos(angle), -math.sin(angle), 0],
                 [math.sin(angle), math.cos(angle), 0],
                 [0, 0, 1]]

    for point in points:
        rotated_2d = matrix_multiplication(rotation_y, point)
        rotated_2d = matrix_multiplication(rotation_x, rotated_2d)
        rotated_2d = matrix_multiplication(rotation_z, rotated_2d)

        distance = 5

        z = 1/(distance - rotated_2d[2][0])
        projection_matrix = [[z, 0, 0 ],
                            [0, z, 0]]

        projected2d = matrix_multiplication(projection_matrix, rotated_2d)

        x = int(projected2d[0][0] * scale ) + cube_position[0]
        y = int(projected2d[1][0] * scale ) + cube_position[1]

        projected_points[index] = [x, y]
        pygame.draw.circle(screen, blue, (x, y), 10)
        index += 1

    for m in range(4):
        connect_points(m, (m+1)%4, projected_points)
        connect_points(m+4, (m+1)%4 + 4, projected_points)
        connect_points(m, m+4, projected_points)

    angle += speed
    pygame.display.update()


pygame.quit()
