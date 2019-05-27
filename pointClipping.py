points = [2, 2]
x_min, x_max = 2, 3
y_min, y_max = 1, 4


if (x_min <= points[0] <= x_max) and (y_min <= points[1] <= y_max):
	print('({}, {}) lies inside the clipping window.'.format(points[0], points[1]))
else:
	print('({}, {}) does not lies inside the clipping window.'.format(points[0], points[1]))