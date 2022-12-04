def is_fully_contained(sections):
  contained = False
  left_side = sections[0]
  right_side = sections[1]
  # case left_side inside right_side
  if int(left_side[0]) >= int(right_side[0]) and int(left_side[1]) <= int(right_side[1]):
    contained = True
  # case right_side inside left_side
  if int(right_side[0]) >= int(left_side[0]) and int(right_side[1]) <= int(left_side[1]):
    contained = True
  return contained



input_lines = open("input.txt")
pairs = []
for m in input_lines:
  elves_input = list(map(lambda x : x.split("-"), m.strip().split(",")))
  pairs.append(elves_input)
#print(pairs)

count = 0
id = 1
for section in pairs:
  if is_fully_contained(section):
    print("at", id, "found fully contained", section, count)
    count += 1
  id += 1
print(count)
  
  
  
