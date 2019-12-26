n = int(input('Enter size of board: '))

def printBoard(board):
	count = 1
	for row in board:
		print(count, end=' ')
		for col in row:
			print(col, end=" ")
		count += 1
		print('')


def isSafe(board, row, col):
	for i in range(row):
		if board[i][col] == 'Q':
			return False

	for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
		if board[i][j] == 'Q':
			return False	

	for i, j in zip(range(row, -1, -1), range(col, n, 1)):
		if board[i][j] == 'Q':
			return False


	return True


def solveNQx(board, row):
	if row >= n:
		return True


	for i in range(n):
		if isSafe(board, row, i):
			board[row][i] = 'Q'

			if solveNQx(board, row + 1):
				return True

			board[row][i] = '-'

	return False


def solveNQ():
	board = list()
	for i in range(n):
		row = list()
		for j in range(n):
			row.append('-')
		board.append(row)


	if solveNQx(board, 0) == False:
		print('No Solution')
	else:
		for i in [' '] + list(range(1, n + 1)):
			print(i, end=' ')
		print('')
		printBoard(board)


solveNQ()
