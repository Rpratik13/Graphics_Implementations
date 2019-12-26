from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
from math import *

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2f(x, y)
    glVertex2f(180 - x, y)
    glVertex2f(180 + x, -y)
    glVertex2f(360 - x, -y)
    glEnd()


def circle():
    for y in range(0.001, 1.001, 0.001):
        x = degrees(asin(y))
        plot(x, y)

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Sin Drawing')
    gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(circle)
    glutMainLoop()

if __name__ == '__main__':
    main()
