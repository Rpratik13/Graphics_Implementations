from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys

original_points = [[-1, 0], [-1, 7], [2, 4], [2, 1]]
x_min, y_min = -2, 2
x_max, y_max = 2, 5

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

def inbetween(start, end):
    if start[0] == end[0]:
        for i in range(len(original_points)):
            if original_points[i][0] == original_points[(i + 1) % len(original_points)][0] == start[0] and ((original_points[i][1] <= start[1] <= original_points[(i + 1) % len(original_points)][1] and original_points[i][1] <= end[1] <= original_points[(i + 1) % len(original_points)][1]) or (original_points[i][1] >= start[1] >= original_points[(i + 1) % len(original_points)][1] and original_points[i][1] >= end[1] >= original_points[(i + 1) % len(original_points)][1])):
                return True

    else:
        for i in range(len(original_points)):
            if original_points[i][1] == original_points[(i + 1) % len(original_points)][1] == start[1] and ((original_points[i][0] <= start[0] <= original_points[(i + 1) % len(original_points)][0] and original_points[i][0] <= end[0] <= original_points[(i + 1) % len(original_points)][0]) or (original_points[i][0] >= start[0] >= original_points[(i + 1) % len(original_points)][0] and original_points[i][0] >= end[0] >= original_points[(i + 1) % len(original_points)][0])):
                return True
    return False


def leftClipper(start, end):
    clipped = list()
    if end[0] != start[0]:
        m = (end[1] - start[1]) / (end[0] - start[0])
    else:
        m = float('inf')

    if start[0] < x_min and x_min <= end[0]:
        y = end[1] - m * (end[0] - x_min)
        clipped.append([x_min, y])
        clipped.append(end)

    elif start[0] >= x_min and end[0] >= x_min:
        clipped.append(end)

    elif start[0] >= x_min and end[0] < x_min:
        y = end[1] - m * (end[0] - x_min)
        clipped.append([x_min, y])

    return clipped


def rightClipper(start, end):
    clipped = list()
    if end[0] != start[0]:
        m = (end[1] - start[1]) / (end[0] - start[0])
    else:
        m = float('inf')

    if start[0] > x_max and end[0] <= x_max:
        y = end[1] - m * (end[0] - x_max)
        clipped.append([x_max, y])
        clipped.append(end)

    elif start[0] <= x_max and end[0] <= x_max:
        clipped.append(end)

    elif start[0] <= x_max and end[0] > x_max:
        y = end[1] - m * (end[0] - x_max)
        clipped.append([x_max, y])

    return clipped


def bottomClipper(start, end):
    clipped = list()
    if end[0] != start[0]:
        m = (end[1] - start[1]) / (end[0] - start[0])
    else:
        m = float('inf')

    if start[1] < y_min and end[1] >= y_min:
        x = end[0] + (y_min - end[1]) / m
        clipped.append([x, y_min])
        clipped.append(end)

    elif start[1] >= y_min and end[1] >= y_min:
        clipped.append(end)

    elif start[1] >= y_min and end[1] < y_min:
        x = end[0] + (y_min - end[1]) / m
        clipped.append([x, y_min])

    return clipped


def topClipper(start, end):
    clipped = list()
    if end[0] != start[0]:
        m = (end[1] - start[1]) / (end[0] - start[0])
    else:
        m = float('inf')

    if start[1] > y_max and end[1] <= y_max:
        x = end[0] + (y_max - end[1]) / m
        clipped.append([x, y_max])
        clipped.append(end)

    elif start[1] <= y_max and end[1] <= y_max:
        clipped.append(end)

    elif start[1] <= y_max and end[1] > y_max:
        x = end[0] + (y_max - end[1]) / m
        clipped.append([x, y_max])

    return clipped          


def calcDiv(points):
    div = max(abs(x_min), abs(x_max), abs(y_min), abs(y_max))
    for i in points:
        for j in i:
            div = max(div, abs(j))
    return (div + 1)


def drawPoints(start, end, div, color='r'):
    glBegin(GL_LINES)
    glColor(1, 0, 0, 0)
    if color == 'g':
        glColor(0, 1, 0, 0)

    glVertex2f(start[0] / div, start[1] / div)
    glVertex2f(end[0] / div, end[1] / div)
    glColor(1, 1, 1, 0)
    glEnd()


def sutherlandHodgeman():
    drawAxes()
    plotted = list()
    points = original_points
    div = calcDiv(points)
    drawClippingWindow(div)
    for i in range(len(points)):
        drawPoints(points[i], points[(i + 1) % len(points)], div)

    temp_points = list()
    for i in range(len(points)):
        clipped = leftClipper(points[i], points[(i + 1) % len(points)])
        temp_points.extend(clipped)
    points = temp_points

    temp_points = list()
    for i in range(len(points)):
        clipped = rightClipper(points[i], points[(i + 1) % len(points)])
        temp_points.extend(clipped)
    points = temp_points

    temp_points = list()
    for i in range(len(points)):
        clipped = bottomClipper(points[i], points[(i + 1) % len(points)])
        temp_points.extend(clipped)
    points = temp_points

    temp_points = list()
    for i in range(len(points)):
        clipped = topClipper(points[i], points[(i + 1) % len(points)])
        temp_points.extend(clipped)
    points = temp_points

    for i in range(len(points)):
        if ((points[i][0] != points[(i + 1) % len(points)][0]) and (points[i][1] != points[(i + 1) % len(points)][1])) or inbetween(points[i], points[(i + 1) % len(points)]) :
            drawPoints(points[i], points[(i + 1) % len(points)], div, color='g')
    print(points)
    glutSwapBuffers()

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA|GLUT_DOUBLE)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(350, 150)
    glutCreateWindow(b'Polygon Clipping')
    # gluOrtho2D(-50, 50, -50, 50)
    glutDisplayFunc(sutherlandHodgeman)
    glutMainLoop()


if __name__ == '__main__':
    main()