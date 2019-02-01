mazeFile = open('maze2.txt', 'r')
rowsInMaze = 0
mazeList = []
for line in mazeFile:
    rowList = []
    col = 0
    for ch in line[:-1]:
        rowList.append(ch)
        if ch == 'S':
            startRow = rowsInMaze
            startCol = col
        col = col + 1
    rowsInMaze += 1
    mazeList.append(rowList)
columnsInMaze = len(rowList)
print(columnsInMaze)
print(rowsInMaze)