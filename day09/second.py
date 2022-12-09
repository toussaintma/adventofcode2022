
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
    if abs(hy - ty) > 1 and abs(hx - tx) > 1:
      tx = int(hx - (hx - tx)/abs(hx - tx) * 1)
      ty = int(hy - (hy - ty)/abs(hy - ty) * 1)
    elif abs(hy - ty) > 1:
      tx = hx
      ty = int(hy - (hy - ty)/abs(hy - ty) * 1)
    elif abs(hx - tx) > 1:
      tx = int(hx - (hx - tx)/abs(hx - tx) * 1)
      ty = hy
    else:
      pass
  return(tx, ty)
  
def read_command(command, hx, hy):
  if command == "L":
    hx -= 1
  elif command == "U":
    hy += 1
  elif command == "R":
    hx += 1  
  elif command == "D":
    hy -= 1
  return(hx, hy)
  
input_lines = open("input.txt")
commands = [i.strip().split() for i in input_lines]

#print(commands)
all_moves = []
for c in commands:
  all_moves.extend(decompose_moves(c))

knots = [[0, 0] for i in range(10)]
tail_trail = []
tail_trail.append([0,0])

id = 0
for c in all_moves:
  if id < 15:
    print(id, ": Command", c[0], c[1])
    print("  starting from", knots)
  for k in range(len(knots)):
    if k == 0:
      knots[k][0], knots[k][1] = read_command(c[0], knots[k][0], knots[k][1])
    else:
      knots[k][0], knots[k][1] = compute_tail_move(knots[k - 1][0], knots[k - 1][1], 
        knots[k][0], knots[k][1])
      
      if k == len(knots) - 1 and not knots[k] in tail_trail:
        tail_trail.append([knots[k][0], knots[k][1]])
  if id < 15:
    print("  arriving at", knots)
  id += 1
# 6406
print(len(tail_trail))
