from math import *

def matrixMultiply(A, B):
	prod = list()
	for i in range(4):
		row = list()
		for j in range(4):
			sm = 0
			for k in range(4):
				sm += A[i][k] * B[k][j]
			row.append(sm)
		prod.append(row)
	return prod

def translate(points, tx, ty, tz):
	translate_mat = [[1, 0, 0, tx],
					 [0, 1, 0, ty],
					 [0, 0, 1, tz],
					 [0, 0, 0, 1]]
	translated = matrixMultiply(translate_mat, points)
	# print('({}, {}, {})'.format(translated[0][0], translated[1][0], translated[2][0]))
	return translated

def scale(points, sx, sy, sz):
	scale_mat = [[sx, 0, 0, 0],
				 [0, sy, 0, 0],
				 [0, 0, sz, 0],
				 [0, 0, 0, 1]]
	scaled = matrixMultiply(scale_mat, points)
	return scaled


def reflect(points, axis='x'):
	if axis == 'x':
		x = -1
		y = z = 1
	elif axis == 'y':
		x = z = 1
		y = -1
	elif axis == 'z':
		x = y = 1
		z = -1

	reflect = [[x, 0, 0, 0],
			   [0, y, 0, 0],
			   [0, 0, z, 0],
			   [0, 0, 0, 1]]
	reflected = matrixMultiply(reflect, points)
	return reflected


def rotate(points, theta, axis='x'):
	if axis == 'x':
		rotate_mat = [[1, 0, 0, 0],
					  [0, cos(theta), -sin(theta), 0],
					  [0, sin(theta), cos(theta), 0],
					  [0, 0, 0, 1]]
	elif axis == 'y':
		rotate_mat = [[cos(theta), 0, sin(theta), 0],
					  [0, 1, 0, 0],
					  [-sin(theta), 0, cos(theta), 0],
					  [0, 0, 0, 1]]
	elif axis == 'z':
		rotate_mat = [[cos(theta), -sin(theta), 0, 0],
					  [sin(theta), cos(theta), 0, 0],
					  [0, 0, 1, 0],
					  [0, 0, 0, 1]]
	rotated = matrixMultiply(rotate_mat, points)
	return rotated




if __name__ == '__main__':
	x = 5
	y = 0
	z = 9
	point_mat = [[x],
				 [y],
				 [z],
				 [1]]

	translate(point_mat, tx=5, ty=9, tz=-2)

