grid = [['.', '.', '.', '.', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['.', 'O', 'O', 'O', 'O', 'O'],
 ['O', 'O', 'O', 'O', 'O', '.'],
 ['O', 'O', 'O', 'O', '.', '.'],
 ['.', 'O', 'O', '.', '.', '.'],
 ['.', '.', '.', '.', '.', '.']]

"""print(grid, "\n")


print(grid[1])

print(grid[1][0])


for list in range (len(grid)):
    print(f"{grid[list][0]} ", end='')"""

"""for lists in grid:
    count_list =+ 1
    print("Count is", count_list)
    print(lists)
    print("\nList: \n\n")
    for obj in lists:
        count_obj =+ 1
        print("obj num is", count_obj)
        print(obj, end='')
    print("\nRow: \n\n")"""

"""for x in range (len(grid)):
    #print(x)
    #print(grid[x])
    for y in range (len(grid)) :
        print(f"[{x}][{y}]")
        print(grid[x][y], end='')
        x += 1
    print("\n\n")"""



"""for row in range (len(grid)):
    for item in range(len(grid)):
        print(f"{grid[item][row]} ", end='')
       
    print("\n")"""

for col in range(len(grid[0])):
    for row in grid:
        print(row[col], end='')
    print()



