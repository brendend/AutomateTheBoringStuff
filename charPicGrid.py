# grid = [['.', '.', '.', '.', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['.', 'O', 'G', 'O', 'O', 'O'],
#         ['O', 'O', 'O', 'O', 'O', '.'],
#         ['O', 'O', 'O', 'O', '.', '.'],
#         ['.', 'O', 'O', '.', '.', '.'],
#         ['.', '.', '.', '.', '.', '.']]
        
# rows = len(grid) # Number of elements in the list
# cols = len(grid[0]) # Number of elements in every single element in the list

# for j in range(6):
#     for i in range(9):
#         print(grid[i][j], end='')
#     print()

# print(str(rows)) #9
# print(str(cols)) #6

# for x in range(3):
#     print(grid[x][x])

gridx = [['a', 'b', 'c', 'd', 'e', 'f'],
        ['g', 'h', 'i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p', 'q', 'r'],
        ['s', 't', 'u', 'v', 'w', 'y'],
        ['x', 'z', '1', '2', '3', '4']]
for x in range(5):
    for i in range(6):
        print(gridx[x][i], end='')
    print()
    
