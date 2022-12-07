class Directory:
  def get_heavy_directories(this):
    total = 0
    if this.size <= 100000:
      total = this.size
    for i in this.directories:
      total += i.get_heavy_directories()
#    print("found heavy dir", this.name, total, this.size)
    return(total)  
  
  def get_all_sizes(this, results):
    results.append(this.size)
    for i in this.directories:
      results = i.get_all_sizes(results)
#    print("found", this.get_full_path(), results)
    return(results)    
      
  def update_size(this):
    s = 0
    for i in this.files:
      s += int(i[1])
    for i in this.directories:
      s += i.update_size()  
    this.size = s
    return s
      
  def get_subdirectory(this, directory_name):
    result = None
    for d in this.directories:
      if d.name == directory_name:
        result = d
        break
    return(result)
      
    this.files.append([file_name, file_size])
  
  def add_file(this, file_name, file_size):
    this.files.append([file_name, file_size])
    
  def add_directory(this, directory_name):
    new_directory = Directory(this, directory_name)
    this.directories.append(new_directory)
    return(new_directory)
  
  def get_full_path(this):
    if this.mother == None: # bug / not appearing for root path alone
      full_path = this.name
    else:
      next_dir = this.mother
      full_path = next_dir.get_full_path() + "/" + this.name
    return(full_path)
      
    while next_dir != None:
      full_path = "/" + next_dir.name
      next_dir = next_dir.mother
  
  def show_tree(this):
    print("node", this.get_full_path(), this.size)
    for i in this.files:
      print(i[0], i[1])
    for i in this.directories:
      i.show_tree()

  def __init__(this, mother, name):
    this.name = name
    this.mother = mother
    this.files = []
    this.directories = []
    this.size = 0
  
filesystem = Directory(None, "")
current_path = ""
current_directory = filesystem
input_lines = open("input.txt")

for m in input_lines:
  l = m.strip()
  if "$" in l:
    if l.startswith("$ cd "):
      target = l[5:]
      if target == "..":
        if current_path == "":
          print("Error: cannot go up, already in /")
        else:
          current = current_path.split("/")
          current_path = "/".join(current[:-1]) 
          current_directory = current_directory.mother
      elif target == "/":
        current_path = ""
        current_directory = filesystem
      else:
        current_path = current_path + "/" + target 
        existing_directory = current_directory.get_subdirectory(target)
        if existing_directory == None:
          current_directory = current_directory.add_directory(target)
        else:
          current_directory = existing_directory
  else:
    line = l.split()
    if line[0] == "dir":
      current_directory.add_directory(line[1])
    else:
      current_directory.add_file(line[1], line[0])

filesystem.update_size()
#filesystem.show_tree()
objective = 30000000 - (70000000 - filesystem.size)

print("we have to free up", objective)
all_sizes = filesystem.get_all_sizes([])
all_sizes.sort()

result = 0
for i in all_sizes:
  if i > objective:
    result = i
    break
print("let's remove", result, "from", all_sizes)
