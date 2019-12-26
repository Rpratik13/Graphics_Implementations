from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys


xc = int(input('Enter xc: '))
yc = int(input('Enter yc: '))
rx = int(input('Enter rx: '))
ry = int(input('Enter ry: '))

def plot(x, y):
    glBegin(GL_POINTS)
    glVertex2i(x + xc, y + yc)
    glVertex2i(-x + xc, y + yc)
    glVertex2i(x + xc, -y + yc)
    glVertex2i(-x + xc, -y + yc)
    glEnd()


def ellipseDrawing():
    points = list()
    x = 0
    y = ry

    p = (ry ** 2) - (rx ** 2) * ry + (rx ** 2) / 4
    plot(x, y)

    while x * (ry ** 2) < y * (rx ** 2):
        x += 1
        if p < 0:
            p += 2 * (ry ** 2) * x + (ry ** 2)
        else:
            y -= 1
            p += 2 * (ry ** 2) * x + (ry ** 2) - 2 * (rx ** 2) * y

        plot(x, y)

    p = (ry ** 2) * (x ** 2) + (ry ** 2) * (x + 1 / 4) + (rx ** 2) * ((y - 1) ** 2) - (rx * ry) ** 2

    while y != 0:
        y -= 1
        if p < 0:
            x += 1
            p += -2 * (rx ** 2) * y + 2 * (rx ** 2) * x + (rx ** 2)
        else:
            p += -2 * (rx ** 2) * y + (rx ** 2)

        plot(x, y)
    glutSwapBuffers()


def main():
  glutInit(sys.argv)
  glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
  glutInitWindowSize(500, 500)
  glutInitWindowPosition(350, 150)
  glutCreateWindow(b'Ellipse Drawing')
  gluOrtho2D(-50, 50, -50, 50)
  glutDisplayFunc(ellipseDrawing)
  glutMainLoop()

if __name__ == '__main__':
  main()
