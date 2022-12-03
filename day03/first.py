input_file = open("input.txt")
first_comp = []
second_comp = []


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

score = 0
for m in input_file:
  input_line = m.strip()
  comp_len = len(input_line) // 2
  first_comp.append(input_line[0 : comp_len])
  second_comp.append(input_line[comp_len : ])

for i in range(len(first_comp)):
  shared_item = ""
  for c in second_comp[i]:
    if c in first_comp[i] and c not in shared_item:
      shared_item = shared_item + c
      priority = get_priority(c)
      score = score + priority
      print("line", i, "found", c, "with priority", priority, "giving", score, shared_item)
print(first_comp, second_comp)
print(score)
      
  
