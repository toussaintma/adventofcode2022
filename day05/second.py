def move_crates(crates, commands):
  orig = commands[1] - 1
  dest = commands[2] - 1
  count = commands[0]
  substack = []
  for i in range(count):
    substack.append(crates[orig][-1])
    crates[orig] = crates[orig][:-1]
  for i in range(count - 1, -1, -1):
    crates[dest].append(substack[i])
  return

def get_top_crates(crates):
  result = ""
  for c in crates:
    if len(c) > 0:
      result = result + c[-1]
  return result


stacks = [[] for i in range(10)]
input_lines = open("input.txt")
moves = []

for m in input_lines:
  if "[" in m:
    i = 0
    while i < len(m):
      # 1 at 1, 2 at 5, 3 at 9, 4 at 13, 5 at 17
      if m[i] == "[":
        pos = (i + 1) // 4
        stacks[pos].append(m[i + 1])
      i += 1  
  elif "m" in m:
    move_read = []
    lf = m.split("from")
    move_read.append(int(lf[0][4:]))
    lg = lf[1].split("to")
    move_read.append(int(lg[0]))
    move_read.append(int(lg[1]))
    moves.append(move_read)

for temp_stack in stacks:
  temp_stack.reverse()
 

for do_move in moves:
  move_crates(stacks, do_move)

print(get_top_crates(stacks))




