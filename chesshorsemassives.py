y, x = map(int, input().split())
board = [['.' for _ in range(8)] for _ in range(8)]
board[x-1][y-1] = 'K'
moves = [(2, 1),(2, -1),(-2, 1),(-2, -1),(1, 2),(1, -2),(-1, 2),(-1, -2)]
for dx, dy in moves:
    nx, ny = x - 1 + dx, y - 1 + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        board[nx][ny] = '*'
for row in board:
    print(' '.join(row))