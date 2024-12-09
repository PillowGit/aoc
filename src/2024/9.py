from pathlib import Path
from .. import utils as u
from rich import print
from collections import deque

def sln1(input):
  files = deque() # entries are (disk_pos, file_id)
  spaces = deque() # entries are (disk_pos, space_size)
  res = [] # represents the disk at the end :p
  isfile = True
  file_id = 0
  disk_pos = 0

  # Parse/Build disk
  for _, char in enumerate(input):
    if isfile:
      for _ in range(int(char)):
        res.append(file_id)
        files.append((disk_pos, file_id))
        disk_pos += 1
      file_id += 1
    else:
      spaces.append((disk_pos, int(char)))
      for _ in range(int(char)):
        res.append(None)
        disk_pos += 1
    isfile = not isfile

  # Simulate disk moving files
  for disk_pos, file_id in reversed(files):
    for space_idx, (space_pos, space_size) in enumerate(spaces):
      if space_size >= 1 and disk_pos > space_pos:
        res[space_pos] = file_id
        res[disk_pos] = None
        spaces[space_idx] = (space_pos+1, space_size-1)
        break

  # Get answer
  ans = 0
  for i, v in enumerate(res):
    if v is not None:
      ans += i*v

  return ans

def sln2(input):
  files = deque() # entries are (disk_pos, file_size, file_id)
  spaces = deque() # entries are (disk_pos, space_size)
  res = [] # represents the disk at the end :p
  isfile = True
  file_id = 0
  disk_pos = 0

  # Parse/Build disk
  for _, char in enumerate(input):
    if isfile:
      files.append((disk_pos, int(char), file_id))
      for _ in range(int(char)):
        res.append(file_id)
        disk_pos += 1
      file_id += 1
    else:
      spaces.append((disk_pos, int(char)))
      for _ in range(int(char)):
        res.append(None)
        disk_pos += 1
    isfile = not isfile

  # Simulate disk moving
  for disk_pos, file_size, file_id in reversed(files):
    for space_idx, (space_pos, space_size) in enumerate(spaces):
      if space_size >= file_size and disk_pos > space_pos:
        for i in range(file_size):
          res[space_pos+i] = file_id
          res[disk_pos+i] = None
        spaces[space_idx] = (space_pos+file_size, space_size-file_size)
        break

  # Get answer
  ans = 0
  for i, v in enumerate(res):
    if v is not None:
      ans += i*v

  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))