


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
    
#print(register_x)
#for i in range(len(register_x)):
#  print(i, ":", register_x[i])

signal_strength_sum = (20 * register_x[19] + 60 * register_x[59] + 100 * register_x[99] + 140 * register_x[139] + 180 * register_x[179] + 220 * register_x[219])
print(signal_strength_sum)
