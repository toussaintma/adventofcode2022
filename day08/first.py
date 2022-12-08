



grid = []
input_lines = open("input.txt")
for m in input_lines:
  grid.append(m.strip())

line_count = len(grid)
column_count = len(grid[0])

visibility = [["" for c in range(column_count)] for l in range(line_count)]

total_visible = 0
for l in range(line_count):
  for c in range(column_count):
    to_check = grid[l][c]
    item_visible = ["", "", "", ""]
    # checking left
    if c == 0:
      item_visible[0] = "v"
    else: 
      item_visible[0] = "v"
      for i in range(c):
        if grid[l][i] >= to_check:
          item_visible[0] = "n"
          break
    # checking top
    if l == 0:
      item_visible[1] = "v"
    else: 
      item_visible[1] = "v"
      for i in range(l):
        if grid[i][c] >= to_check:
          item_visible[1] = "n"
          break 
    # checking right
    if c == column_count - 1:
      item_visible[2] = "v"
    else: 
      item_visible[2] = "v"
      for i in range(c + 1, column_count):
        if grid[l][i] >= to_check:
          item_visible[2] = "n"
          break 
    # checking down
    if l == line_count:
      item_visible[3] = "v"
    else: 
      item_visible[3] = "v"
      for i in range(l + 1, line_count):
        if grid[i][c] >= to_check:
          item_visible[3] = "n"
          break     
    visibility[l][c] = item_visible[0] + item_visible[1] + item_visible[2] + item_visible[3]
    if "v" in visibility[l][c]:
      total_visible += 1
     
#print(visibility)
print(total_visible)

     
