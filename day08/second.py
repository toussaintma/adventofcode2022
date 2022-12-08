



grid = []
input_lines = open("input.txt")
for m in input_lines:
  grid.append(m.strip())

line_count = len(grid)
column_count = len(grid[0])

scenic_score = [[0 for c in range(column_count)] for l in range(line_count)]

for l in range(line_count):
  for c in range(column_count):
    to_check = grid[l][c]
    distances = [0, 0, 0, 0]
    # checking left
    if c == 0:
      distances[0] = 0
    else: 
      distances[0] = 0
      for i in range(c - 1, -1, -1):
        distances[0] += 1
        if grid[l][i] >= to_check:
          break
    # checking top
    if l == 0:
      distances[1] = 0
    else: 
      distances[1] = 0
      for i in range(l - 1, -1, -1):
        distances[1] += 1
        if grid[i][c] >= to_check:
          break 
    # checking right
    if c == column_count - 1:
      distances[2] = 0
    else: 
      distances[2] = 0
      for i in range(c + 1, column_count):
        distances[2] += 1
        if grid[l][i] >= to_check:
          break
    # checking down
    if l == line_count:
      distances[3] = 0
    else: 
      distances[3] = 0
      for i in range(l + 1, line_count):
        distances[3] += 1
        if grid[i][c] >= to_check:
          break
    #print("found:", distances, "for", l, c)     
    scenic_score[l][c] = distances[0] * distances[1] * distances[2] * distances[3] 

max_score = 0
for i in range(line_count):
  max_local = max(scenic_score[i])
  if max_local > max_score:
    max_score = max_local
     
#print(scenic_score)
print(max_score)

     
