grid = [[0]]
for t in range(21):
    i = t + 1
    #print(t, i, grid)
    print(t,"by",t)
    for y in range(i):
        if y == 0 and t != 0:
            grid[y].append(1)
        elif y != t:
            grid[y].append(grid[y][t-1]+grid[y-1][t])
        else:
            for x in range(t):
                x += 1
                grid[y].append(grid[y][x-1]+grid[y-1][x])
        #print(grid[y])
    #print(grid)
    grid.append([1])
#print(grid)
for h in range(21):
    print(h, grid[h])
    print(grid[20][20])
