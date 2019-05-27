from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys

xc, yc = 5, 1
r = 20

def plot(x, y):
	glBegin(GL_POINTS)
	glVertex2i(x + xc, y + yc)
	glVertex2i(-x + xc, y + yc)
	glVertex2i(x + xc, -y + yc)
	glVertex2i(-x + xc, -y + yc)
	glVertex2i(y + xc, x + yc)
	glVertex2i(-y + xc, x + yc)
	glVertex2i(y + xc, -x + yc)
	glVertex2i(-y + xc, -x + yc)
	glEnd()


def circle():
	x = 0
	y = r

	p = 1 - r

	while x != y:
		print('x')
		x += 1
		if p < 0:
			plot(x, y)
			p += 2 * x + 1
		else:
			y -= 1
			plot(x, y)
			p += 2 * (x - y) + 1
	glutSwapBuffers()


def main():
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
	glutInitWindowSize(500, 500)
	glutInitWindowPosition(350, 150)
	glutCreateWindow(b'Circle Drawing')
	gluOrtho2D(-50, 50, -50, 50)
	glutDisplayFunc(circle)
	glutMainLoop()

if __name__ == '__main__':
	main()