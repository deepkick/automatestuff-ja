#! python3
# -*- coding: utf-8 -*-

# 演習プロジェクト 4.10.2 文字絵グリッド

def print_grid(grid):
    width = len(grid)
    height = len(grid[0])
    for y in range(height):
        for x in range(width):
            print(grid[x][y], end='')
        print()

grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

print_grid(grid)
