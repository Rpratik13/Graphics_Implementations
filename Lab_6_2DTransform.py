from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math

points = [[20, 20], [20, 40], [40, 40]]
print('Select \n1. Translate \n2. Rotate \n3. Scale')
select = int(input('Enter your selection: '))
print('\n')

def matrixMultiply(A, B):
    prod = list()
    for i in range(3):
        sm = 0
        for j in range(3):
            sm += A[i][j] * B[j][0]
        prod.append(sm)
    return prod[:2]


def translate():
    translated = list()

    translate_mat = [[1, 0, tx],
                     [0, 1, ty],
                     [0, 0, 1]]

    for point in points:
        point_mat = [[point[0]], [point[1]], [1]]
        translated.append(matrixMultiply(translate_mat, point_mat))
    points.extend(translated)



def rotate():
    translated = list()
    theta_rad = math.radians(theta)
    rotate_mat = [[math.cos(theta_rad), -math.sin(theta_rad), 0],
                  [math.sin(theta_rad), math.cos(theta_rad), 0],
                  [0, 0, 1]]
    for point in points:
        point_mat = [[point[0]], [point[1]], [1]]
        translated.append(matrixMultiply(rotate_mat, point_mat))
    points.extend(translated)


def scale():
    translated = list()
    scale_mat = [[sx, 0, 0],
                 [0, sy, 0],
                 [0, 0, 1]]
    for point in points:
        point_mat = [[point[0]], [point[1]], [1]]
        translated.append(matrixMultiply(scale_mat, point_mat))
    points.extend(translated)


if select == 1:
    tx = int(input('Enter tx: '))
    ty = int(input('Enter ty: '))
    translate()
elif select == 2:
    xc = int(input('Enter xc: '))
    yc = int(input('Enter yc: '))
    theta = int(input('Enter angle of rotation: '))
    rotate()
elif select == 3:
    sx = int(input('Enter sx: '))
    sy = int(input('Enter sy: '))
    sz = int(input('Enter sz: '))
    scale()


def drawAxes():
    glBegin(GL_LINES)
    glVertex2i(1, 0)
    glVertex2i(-1, 0)
    glVertex2i(0, 1)
    glVertex2i(0, -1)
    glEnd()

def calcDiv():
    div = 0
    for point in points:
        div = max(div, point[0], point[1])
    return div * 1.05

def drawPolygon():
    drawAxes()
    div = calcDiv()
    count = 0
    glBegin(GL_TRIANGLES)
    for point in points:
        glVertex2f(point[0] / div, point[1] / div)
        count += 1
    glEnd()
    glutSwapBuffers()





def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'2D Transformations')
    glutDisplayFunc(drawPolygon)
    glutMainLoop()


if __name__ == '__main__':
    main()
