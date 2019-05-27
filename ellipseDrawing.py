from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

xc, yc = 20, 10
rx, ry = 9, 15
div = max(abs(rx) + abs(xc), abs(ry) + abs(yc)) + 1


def plot(x, y):
	glBegin(GL_POINTS)
	glVertex2f((x + xc) / div, (y + yc) / div)
	glVertex2f((-x + xc) / div, (y + yc) / div)
	glVertex2f((x + xc) / div, (-y + yc) / div)
	glVertex2f((-x + xc) / div, (-y + yc) / div)
	glEnd()


def drawAxes():
	glColor(0, 0, 1, 0)
	glBegin(GL_LINES)
	glVertex2i(1, 0)
	glVertex2i(-1, 0)
	glVertex2i(0, 1)
	glVertex2i(0, -1)
	glEnd()
	glColor(1, 1, 1, 0)

def ellipse():
	drawAxes()
	glBegin(GL_POINTS)
	glVertex2f(xc / div, yc / div)
	glEnd()
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
	# gluOrtho2D(-50, 50, -50, 50)
	glutDisplayFunc(ellipse)
	glutMainLoop()

if __name__ == '__main__':
	main()