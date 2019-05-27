import math

def matrixMultiply(A, B):
	prod = list()
	for i in range(4):
		row = list()
		sm = 0
		for j in range(4):
			sm += A[i][j] * B[j][0]
		row.append(sm)
		prod.append(row)
	return prod


def translate(points, tx, ty, tz):
	translate_mat = [[1, 0, 0, tx],
					 [0, 1, 0, ty],
					 [0, 0, 1, tz],
					 [0, 0, 0, 1]]
	translated = matrixMultiply(translate_mat, points)
	print('({}, {}, {})'.format(translated[0][0], translated[1][0], translated[2][0]))
	return translated



if __name__ == '__main__':
	x = 5
	y = 0
	z = 9
	point_mat = [[x],
				 [y],
				 [z],
				 [1]]

	translate(point_mat, tx=5, ty=9, tz=-2)

