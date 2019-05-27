from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import math
import time

start_point = [0, -20]
end_point = [15, 3] 
div = max(max([abs(i) for i in start_point]), max([abs(i) for i in end_point])) + 1


def drawAxes():
    glColor(0, 0, 1, 0)
    glBegin(GL_LINES)
    glVertex2i(1, 0)
    glVertex2i(-1, 0)
    glVertex2i(0, 1)
    glVertex2i(0, -1)
    glEnd()
    glColor(1, 1, 1, 1)


def direct():
    drawAxes()
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    if dx != 0:
        m = dy / dx
    else:
        m = float('inf')
    c = start_point[1] - m * start_point[0]

    x = start_point[0]
    y = start_point[1]
    glBegin(GL_POINTS)
    if m < 1:
        while x != end_point[0]:
            glVertex2f(x / div, y / div)
            if dx < 0:
                x -= 1
            else:
                x += 1
            y = m * x + c
    else:

        while y != end_point[1]:
            glVertex2f(x / div, y / div)
            if dy < 0:
                y -= 1
            else:
                y += 1
            x = (y - c) / m
    glVertex2f(x / div, y / div)
    glEnd()
    glutSwapBuffers()


def DDA():   
    drawAxes()
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    
    x = start_point[0]
    y = start_point[1]

    stepsize = max(abs(dx), abs(dy))
    x_inc = dx / stepsize
    y_inc = dy / stepsize

    glBegin(GL_POINTS)  
    for _ in range(stepsize):
        glVertex2f(x / div, y / div)
        x += x_inc
        y += y_inc
    glVertex2f(x / div, y / div)
    glEnd()
    glutSwapBuffers()


def bresenham():
    drawAxes()
    dx = end_point[0] - start_point[0]
    dy = end_point[1] - start_point[1]
    m = dy / dx

    if abs(m) < 1:
        P1 = abs(dy)
        P2 = abs(dx)
        if dx < 0:
            x_inc = -1
        else:
            x_inc = 1
        y_inc = 0
    else:
        P1 = abs(dx)
        P2 = abs(dy)
        if dy < 0:
            y_inc = -1
        else:
            y_inc = 1
        x_inc = 0

    if dy < 0:
        y_inc2 = -1
    else:
        y_inc2 = 1

    if dx < 0:
        x_inc2 = -1
    else:
        x_inc2 = 1

    P = 2 * P1 - P2

    x = start_point[0]
    y = start_point[1]
    glBegin(GL_POINTS)
    while x != end_point[0] and y != end_point[1]:
        glVertex2f(x / div, y / div)
        if P < 0:
            x += x_inc
            y += y_inc
            P += 2 * P1
        else:
            x += x_inc2
            y += y_inc2
            P += 2 * (P1 - P2)

    glVertex2f(x / div, y / div)
    glEnd()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Line Drawing')
    # gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(direct)
    glutMainLoop()

if __name__ == '__main__':
    main()