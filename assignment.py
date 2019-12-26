from math import *
from Dtransform import *

def mulPoints(tr_mat, point):
	ans = list()
	for row in tr_mat:
		sm = 0
		for i, j in zip(row, point):
			sm += i * j
		ans.append(sm)
	return ans


		
def printMat(matrix):
	for row in range(len(matrix)):
		print('|', end=' ')
		for col in range(len(matrix[0])):
			print('{0:.2f}'.format(matrix[row][col]), end=' ')
		print('|')
	print('\n')


points = [[2, 1, 0], [3, 3, 1]]
v = list()
u = list()

for i, j in zip(points[0], points[1]):
	v.append(j - i)

for x in v:
	u.append(x / (sqrt(v[0] ** 2 + v[1] ** 2 + v[2] ** 2)))


point = [[1, 0, 0, 0],
		 [0, 1, 0, 0],
		 [0, 0, 1, 0],
		 [0, 0, 0, 1]]
print('T(x1, y1, z1).Rx(-alpha)')
T = translate(point, points[0][0], points[0][1], points[0][2])
alpha = acos(u[2] / sqrt(u[1] ** 2 + u[2] ** 2))
Rx = rotate(point, -alpha, axis='x')
Tr = matrixMultiply(T, Rx)

printMat(Tr)

print('T(x1, y1, z1).Rx(-alpha).Ry(-beta)')
Ry = [[sqrt(5/6), 0, sqrt(1/6), 0],
	  [0, 1, 0, 0],
	  [-sqrt(1/6), 0, sqrt(5/6), 0],
	  [0, 0, 0, 1]]
Tr = matrixMultiply(Tr, Ry)
printMat(Tr)

print('T(x1, y1, z1).Rx(-alpha).Ry(-beta).Rz(90)')
Rz = rotate(point, radians(90), axis='z')
Tr = matrixMultiply(Tr, Rz)

printMat(Tr)
print('T(x1, y1, z1).Rx(-alpha).Ry(-beta).Rz(90).Ry(beta)')
Ry = [[sqrt(5/6), 0, -sqrt(1/6), 0],
	  [0, 1, 0, 0],
	  [sqrt(1/6), 0, sqrt(5/6), 0],
	  [0, 0, 0, 1]]
Tr = matrixMultiply(Tr, Ry)
printMat(Tr)


print('T(x1, y1, z1).Rx(-alpha).Ry(-beta).Rz(90).Ry(beta).Rx(alpha)')
Rx = rotate(point, alpha, axis='x')
Tr = matrixMultiply(Tr, Rx)

printMat(Tr)

print('T(x1, y1, z1).Rx(-alpha).Ry(-beta).Rz(90).Ry(beta).Rx(alpha).T(-x1, -y1, -z1)')
T = translate(point, -points[0][0], -points[0][1], -points[0][2])
Tr = matrixMultiply(Tr, T)

printMat(Tr)


cube_points = [[0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 1], [1, 0, 0, 1], [1, 0, 1, 1], [1, 1, 0, 1], [1, 1, 1, 1]]

for i in cube_points:
	rotated = mulPoints(Tr, i)
	print('({0}, {1}, {2}) -> ({3:.2f}, {4:.2f}, {5:.2f})'.format(i[0], i[1], i[2], rotated[0], rotated[1], rotated[2]))