from Word_Search_Funcs import getWord
grid = open("grid.txt").read().splitlines()

colLen = len(grid)
rowLen = len(grid[0])
print("Grid imported with each row having length", rowLen, "and", colLen, "rows")

for i in range(len(grid)):
    # print(grid[i])
    grid[i] = grid[i].lower()
    if rowLen != len(grid[i]):
        raise Exception("Grid rows are not the same length")
    #grid[i] = list(grid[i])

# print(grid)

searchRow = 0
searchCol = 0

# Scan through each letter in grid
for i in range(colLen):
    for j in range(rowLen):
        getWord(grid, i, j, colLen, rowLen)