
def decompose_moves(command):
  count = int(command[1])
  result = []
  for i in range(count):
    result.append([command[0], 1])
  return(result)

def compute_tail_move(hx, hy, tx, ty): 
  if hx == tx and hy == ty:
    pass
  elif hx == tx:
    if abs(hy - ty) > 1:
      ty = int(hy - (hy - ty)/abs(hy - ty) * 1)
  elif hy == ty:
    if abs(hx - tx) > 1:
      tx = int(hx - (hx - tx)/abs(hx - tx) * 1)
  else:
    if abs(hy - ty) > 1:
      tx = hx
      ty = int(hy - (hy - ty)/abs(hy - ty) * 1)
    elif abs(hx - tx) > 1:
      tx = int(hx - (hx - tx)/abs(hx - tx) * 1)
      ty = hy
    else:
      pass
  return(tx, ty)
  
  
input_lines = open("input.txt")
commands = [i.strip().split() for i in input_lines]

#print(commands)
all_moves = []
for c in commands:
  all_moves.extend(decompose_moves(c))

head_x = head_y = 0
tail_x = tail_y = 0  
tail_trail = []
tail_trail.append([tail_x, tail_y])

id = 0
for c in all_moves:
  if id < 15:
    print(id, ": Command", c[0], c[1])
    print("  starting from", head_x, head_y, tail_x, tail_y) 
  if c[0] == "L":
    head_x -= 1
  elif c[0] == "U":
    head_y += 1
  elif c[0] == "R":
    head_x += 1  
  elif c[0] == "D":
    head_y -= 1
  tail_x, tail_y = compute_tail_move(head_x, head_y, tail_x, tail_y)
  if not [tail_x, tail_y] in tail_trail:
    tail_trail.append([tail_x, tail_y])
  if id < 15:
    print("  going to", head_x, head_y, tail_x, tail_y)
  id += 1

print(len(tail_trail))
