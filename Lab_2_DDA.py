from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

no_of_points = int(input('How many points do you want to enter?: '))
while no_of_points < 2:
    print('Atleast 2 points are required. \n')
    no_of_points = int(input('How many points do you want to enter?: '))

points = list()
for _ in range(no_of_points):
    point = [int(i) for i in input('Enter P{}(x, y): '.format(_)).split(',')]
    points.append(point)
colors = list()   
    

def calcDiv():
    div = 0
    for point in points:
        for i in point:
            div = max(div, abs(i))
    return div + 1


def drawAxes():
    glBegin(GL_LINES)
    glVertex2i(1, 0)
    glVertex2i(-1, 0)
    glVertex2i(0, 1)
    glVertex2i(0, -1)
    glEnd()


def setColor():
    if len(colors) == len(points) - 2:
        if colors[-1] == 'g':
            glColor(0, 0, 1, 0)
        else:
            glColor(0, 1, 0, 0)
    elif len(colors) % 3 == 0:
        glColor(1, 0, 0, 0)
        colors.append('r')
    elif len(colors) % 3 == 1:
        glColor(0, 1, 0, 0)
        colors.append('g')
    else:
        glColor(0, 0, 1, 0)
        colors.append('b')


def DDA():
    drawAxes()
    div = max(calcDiv(), 250)   
    glBegin(GL_POINTS)
    for i in range(len(points) - 1):
        dx = points[i + 1][0] - points[i][0]
        dy = points[i + 1][1] - points[i][1]
        
        x = points[i][0]
        y = points[i][1]

        stepsize = max(abs(dx), abs(dy))
        x_inc = dx / stepsize
        y_inc = dy / stepsize

        setColor()
        for _ in range(stepsize):
            glVertex2f(x / div, y / div)
            x += x_inc
            y += y_inc
        glVertex2f(x / div, y / div)
    glEnd()
    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'DDA Line Drawing')
    glutDisplayFunc(DDA)
    glutMainLoop()

if __name__ == '__main__':
    main()