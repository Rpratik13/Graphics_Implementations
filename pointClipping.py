from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

points = [[3, 2], [3, 1], [0, 3], [12, 2], [-1, 2]]
x_min, x_max = 2, 4
y_min, y_max = 1, 4

def drawAxes():
    glColor(0, 0, 1, 0)
    glBegin(GL_LINES)
    glVertex2i(1, 0)
    glVertex2i(-1, 0)
    glVertex2i(0, 1)
    glVertex2i(0, -1)
    glEnd()
    glColor(1, 1, 1, 1)


def drawClippingWindow(div):
    glBegin(GL_LINE_LOOP)
    glVertex2f(x_min / div, y_min / div)
    glVertex2f(x_max / div, y_min / div)
    glVertex2f(x_max / div, y_max / div)
    glVertex2f(x_min / div, y_max / div)
    glEnd()


def calcDiv(points):
	div = max(abs(x_min), abs(x_max), abs(y_min), abs(y_max))
	for i in points:
		for j in i:
			div = max(div, abs(j))

	return div + 1

def pointClipping():
	drawAxes()
	div = calcDiv(points)
	drawClippingWindow(div)
	for point in points:
		glBegin(GL_POINTS)
		if (x_min <= point[0] <= x_max) and (y_min <= point[1] <= y_max):
			# print('({}, {}) lies inside the clipping window.'.format(point[0], point[1]))
			glColor(0, 1, 0, 0)
			glVertex2f(point[0] / div, point[1] / div)
		else:
			# print('({}, {}) does not lies inside the clipping window.'.format(point[0], point[1]))
			glColor(1, 0, 0, 0)
			glVertex2f(point[0] / div, point[1] / div)
		glEnd()
	glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Point Clipping')
    # gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(pointClipping)
    glutMainLoop()


if __name__ == '__main__':
	main()