import math

def matrixMultiply(A, B):
	prod = list()
	for i in range(3):
		row = list()
		sm = 0
		for j in range(3):
			sm += A[i][j] * B[j][0]
		row.append(sm)
		prod.append(row)
	return prod


def translate(points, tx, ty):
	translate_mat = [[1, 0, tx],
					 [0, 1, ty],
					 [0, 0, 1]]
	translated = matrixMultiply(translate_mat, points)
	print('({}, {})'.format(translated[0][0], translated[1][0]))
	return translated


def rotate(points, theta):
	theta = math.radians(theta)
	rotate_mat = [[math.cos(theta), -math.sin(theta), 0],
				  [math.sin(theta), math.cos(theta), 0],
				  [0, 0, 1]]
	translated = matrixMultiply(rotate_mat, points)
	if abs(translated[0][0]) < 0.001:
		translated[0][0] = 0
	if abs(translated[1][0]) < 0.001:
		translated[1][0] = 0
	print('({}, {})'.format(translated[0][0], translated[1][0]))
	return translated


def scale(points, sx, sy):
	scale_mat = [[sx, 0, 0],
				 [0, sy, 0],
				 [0, 0, 1]]
	translated = matrixMultiply(scale_mat, points)
	print('({}, {})'.format(translated[0][0], translated[1][0]))
	return translated


def reflect(points, about='x')
	if about == 'x':
		reflect_mat = [[-1, 0, 0],
					   [0, 1, 0],
					   [0, 0, 1]]

	elif about == 'y':
		reflect_mat = [[1, 0, 0],
					   [0, -1, 0],
					   [0, 0, 1]]

	else:
		reflect_mat = [[-1, 0, 0],
					   [0, -1, 0],
					   [0, 0, 1]]

	translated = matrixMultiply(reflect_mat, points)
	print('({}, {})'.format(translated[0][0], translated[1][0]))
	return translated

	
def shear(points, shx, shy, ref=0, axis='x'):
	if axis == 'x':
		shear_mat = [[1, shx, -shx * ref],
					 [0, 1, 0],
					 [0, 0, 1]]

	elif axis == 'y':
		shear_mat = [[1, 0, 0],
					 [shy, 1, -shy * ref],
					 [0, 0, 1]]

	translated = matrixMultiply(shear_mat, points)
	print('({}, {})'.format(translated[0][0], translated[1][0]))
	return translated

	


if __name__ == '__main__':
	x = 5
	y = 0
	point_mat = [[x],
				 [y],
				 [1]]

	rotate(point_mat, -90)