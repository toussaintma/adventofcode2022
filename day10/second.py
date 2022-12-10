def is_drawable(position, x):
  result = False
  if abs(x - position) <= 1:
    result = True
  return(result)


input_lines = open("input.txt")
lines = [l.strip().split() for l in input_lines]

commands = []
for l in lines:
  if len(l) == 2:
    commands.append(0)
    commands.append(int(l[1]))
  else:
    commands.append(0)

current_x = 1
register_x = [1] # value of register x at the end of a given cycle
for c in commands:
  current_x += c
  register_x.append(current_x)
    
print(len(commands), len(register_x))
for i in range(len(register_x)):
  print(i, ":", register_x[i])

screen = [["#" for i in range(40)] for j in range(6)]

for y in range(0, 6):
  for x in range(0, 40):
    cycle = (x + 1) + 40 * y
    pixel_position = x
    sprite_position = register_x[cycle - 1]
    if is_drawable(pixel_position, sprite_position):
      screen[y][x] = "#"
    else:
      screen[y][x] = "."

for y in range(6):
  for x in range(40):
    print(screen[y][x], sep='', end='',)
  print()
