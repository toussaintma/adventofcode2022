def get_priority(ch):
  result = 0
  init_unicode_index = 0
  init_result_index = 0
  
  if ch.isupper():
    init_unicode_index = ord("A")
    init_result_index = 27
  else:
    init_unicode_index = ord("a")
    init_result_index = 1
  result = ord(ch) - init_unicode_index + init_result_index
  return result

input_file = open("input.txt")
first_items = []
second_items = []
third_items = []

score = 0
sack = 0
for m in input_file:
  input_line = m.strip()
  if sack == 0:
    first_items.append(input_line)
    sack += 1
  elif sack == 1:
    second_items.append(input_line)
    sack += 1
  elif sack == 2:
    third_items.append(input_line)
    sack = 0
print(first_items)
print(second_items)
print(third_items)

print("doing first & second")
shared_firstsecond = []
for i in range(len(first_items)):
  shared_item = ""
  for c in second_items[i]:
    if c in first_items[i] and c not in shared_item:
      shared_item = shared_item + c
      print("line", i, "found", c, shared_item)
  shared_firstsecond.append(shared_item)
print(shared_firstsecond)

print("doing second & third")
shared_secondthird = []
for i in range(len(first_items)):
  shared_item = ""
  for c in third_items[i]:
    if c in shared_firstsecond[i] and c not in shared_item:
      shared_item = shared_item + c
      print("line", i, "found", c, shared_item)
  shared_secondthird.append(shared_item)
print(shared_secondthird)

for i in range(len(shared_secondthird)):
  for j in shared_secondthird[i]:
    score = score + get_priority(j)  

print(score)
      
  
