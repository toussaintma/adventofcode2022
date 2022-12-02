def standardize(shape):
  result = shape
  if shape == "X": #Rock
    result = "A"
  elif shape == "Y": #Paper
    result = "B"
  elif shape == "Z": #Scissors
    result = "C"
  return result

def shape_score(shape):
  score = 0
  if shape == "A": #Rock
    score = 1
  elif shape == "B": #Paper
    score = 2
  elif shape == "C": #Scissors
    score = 3
  return score

def win_score(opponent, you):
  score = 0
  if opponent == you:
    score = 3
  elif (opponent == "C" and you == "A") or (opponent == "B" 
    and you == "C") or (opponent == "A" and you == "B"):
    score = 6
  return score

my_score = 0
f = open("input.txt")
for m in f:
  l = m.strip().split()
  l[1] = standardize(l[1])
  this_round = shape_score(l[1]) + win_score(l[0], l[1])
  my_score = my_score + this_round
  print(l, " => ", this_round, " = ", shape_score(l[1]), win_score(l[0], l[1]))
print(my_score)
