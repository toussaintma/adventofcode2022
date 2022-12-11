def is_divisible_by(number, divisor):
  result = False
  if number % divisor == 0:
    result = True
  return(result)
  
def execute_operation(operation, old):
  left_read, op_read, right_read = operation.strip().split()
  left_op = old if left_read == "old" else int(left_read)
  right_op = old if right_read == "old" else int(right_read)  
  
  result = 0
  if op_read == "*":
    result = left_op * right_op
  elif op_read == "+":
    result = left_op + right_op
  return(result)  
  
def show_monkeys(items):
  for m in range(len(items)):
    print("Monkey ", m, ": ", sep="", end="")
    for i in items[m]:
      print(i, end=", ")
    print()  

input_lines = open("input.txt")
lines =[l.strip() for l in input_lines]

items = []
operations = []
tests = []
iftrue = []
iffalse = []

current_items = []
current_operations = ""
current_tests = -1
current_iftrue = -1
current_iffalse = -1
current_monkey = -1

for l in lines:
  if "Monkey" in l:
    current_monkey = int(l.split()[1].split(":")[0])
    current_items = []
    current_operations = ""
    current_tests = -1
    current_iftrue = -1
    current_iffalse = -1
  if "Starting" in l:
    current_items = list(map(int, l[16:].strip().split(", ")))
  if "Operation" in l:
    current_operations = l[17:].strip()
  if "Test" in l:
    current_tests = int(l[19:].strip())
  if "true" in l:
    current_iftrue = int(l[24:].strip())
  if "false" in l:
    current_iffalse = int(l[26:].strip())
    items.append(current_items)
    operations.append(current_operations)
    tests.append(current_tests)
    iftrue.append(current_iftrue)
    iffalse.append(current_iffalse)

show_monkeys(items)

monkey_activity = [0 for i in range(len(items))]

for throw_round in range(1, 21):
  for m in range(len(items)):
    to_delete = len(items[m])
    for i in items[m]:
      monkey_activity[m] += 1
      worry_level = execute_operation(operations[m], i) // 3
      if is_divisible_by(worry_level, tests[m]):
        items[iftrue[m]].append(worry_level)
      else:
        items[iffalse[m]].append(worry_level)
    for i in range(to_delete):
      del(items[m][0])
  print("After round", throw_round)
  show_monkeys(items)    
monkey_activity.sort(reverse=True)
print(monkey_activity[0] * monkey_activity[1])

