def is_all_different(buffer):
  result = True
  for c in buffer:
    if buffer.count(c) > 1:
      result = False
  return(result)

def is_start_marker(buffer):
  result = False
  if len(buffer) == 4 and is_all_different(buffer):
    result = True
  return(result)

input_lines = open("input.txt")
first_markers = []

for m in input_lines:
  line = m.strip()
  id = 1
  buffer = ""

  for c in line:
    if len(buffer) == 4:
      buffer = buffer[1:]
    buffer = buffer + c
    if is_start_marker(buffer):
      first_markers.append(id)
      break
    id += 1

print(first_markers)


