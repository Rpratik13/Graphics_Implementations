from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

points = list()
no_of_data = int(input('Enter no of data: '))


max_y = 0
for i in range(no_of_data):
    y = float(input('Enter y-value for P{}: '.format(i)))
    max_y = max(y, max_y)
    x = i + 1
    points.append([round(x), round(y)])
label_length = len(str(int(max_y)))

# for i in range(12):
#     points.append([i + 1, (i + 1) * 1000])
# label_length = 5
# max_y = 12000

def calcDiv():
    div_x = 250
    div_y = 0
    for point in points:
        div_y = max(div_y, point[1] * 1.05)
    div_x = max(div_x, len(points) * 20 + 10)
    return div_x, div_y


def labels(font, value, x, y):
    glRasterPos2f(x, y)
    text = str(int(value))
    for ch in text :
        glutBitmapCharacter(font, ctypes.c_int(ord(ch)))

def drawAxes():
    div_x, div_y = calcDiv()
    glColor(1, 1, 1, 0)

    start = max_y / 10
    while start <= max_y:
        labels(GLUT_BITMAP_9_BY_15, start, -0.02 * len(str(int(start))), start / div_y)
        start += max_y / 10
    labels(GLUT_BITMAP_9_BY_15, max_y, -0.02 * len(str(int(max_y))), max_y / div_y)

    glBegin(GL_LINES)
    glVertex2i(-1, 0)
    glVertex2i(1, 0)
    glVertex2i(0, -1)
    glVertex2i(0, 1)
    glEnd()




def drawHistogram():
    div_x, div_y = calcDiv()
    color = 'b'
    num = 1
    pos = 0
    for point in points:
        if color == 'b':
            glColor(1, 0, 0, 0)
            color = 'r'
        elif color == 'r':
            glColor(0, 1, 0, 0)
            color = 'g'
        else:
            glColor(0, 0, 1, 0)
            color = 'b'
        start = [point[0], 0]
        glVertex2f(0, point[1])
        BLA([start[0] + (point[0] - 1) * 20, start[1]], [start[0] + (point[0] - 1) * 20, point[1]])
        BLA([point[0] + (point[0] - 1) * 20, point[1]], [point[0] + 10 + (point[0] - 1) * 20, point[1]])
        BLA([point[0] + 10 + (point[0] - 1) * 20, point[1]], [start[0] + 10 + (point[0] - 1) * 20, start[1]])
        if max_y < 10000 and len(points) <= 12:
            labels(GLUT_BITMAP_9_BY_15, point[1], (start[0] + (point[0] - 1) * 20) / div_x, point[1] / div_y)
        if len(points) <= 12:
            glColor(1, 1, 1, 0)
            if num == 1:
                pos = 4
                # labels(GLUT_BITMAP_9_BY_15, num, 4 / div_x, -0.02)
            elif num > 9:
                pos = (num - 1) * 21.2
            else:
                pos += 21
            labels(GLUT_BITMAP_9_BY_15, num, pos / div_x, -0.02)
            num += 1
    drawAxes()
    glutSwapBuffers()


def BLA(start, end):

    div_x, div_y = calcDiv()
    dx = end[0] - start[0]
    dy = end[1] - start[1]

    if dx != 0:
        m = dy / dx
    else:
        if dy > 0:
            m = float('inf')
        else:
            m = -float('inf')


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

    x = start[0]
    y = start[1]
    glBegin(GL_POINTS)
    glVertex2f(x / div_x, y / div_y)
    while x != end[0] or y != end[1]:

        if P < 0:
            x += x_inc
            y += y_inc
            P += 2 * P1
        else:
            x += x_inc2
            y += y_inc2
            P += 2 * (P1 - P2)
        glVertex2f(x / div_x, y / div_y)
    glEnd()






def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Histogram')
    gluOrtho2D(-0.02 * label_length, 1, -0.03, 1)
    glutDisplayFunc(drawHistogram)
    glutMainLoop()

if __name__ == '__main__':
    main()
