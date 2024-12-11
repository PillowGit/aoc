from pathlib import Path
from .. import utils as u
from rich import print
from collections import defaultdict
import itertools

# Wrong 412
def sln1(input):
  m, n = len(input), len(input[0])

  frequencies = defaultdict(list)
  for i in range(m):
    for j in range(n):
      if input[i][j] != '.':
        frequencies[input[i][j]].append((i, j))
  
  all_nodes = set()
  for locations in frequencies.values():
    for (x1, y1), (x2, y2) in itertools.permutations(locations, 2):
      all_nodes.add((2 * x1 - x2 ,2 * y1 - y2))

  return sum(int(x in range(m) and y in range(n)) for x, y in all_nodes)
        

def sln2(input):
  m, n = len(input), len(input[0])

  frequencies = defaultdict(list)
  for i in range(m):
    for j in range(n):
      if input[i][j] != '.':
        frequencies[input[i][j]].append((i, j))
  
  all_nodes = set()
  for locations in frequencies.values():
    for (x1, y1), (x2, y2) in itertools.combinations(locations, 2):
      res = set()
      dx = x2 - x1
      dy = y2 - y1
      x, y = x1, y1
      while x in range(m) and y in range(n):
        res.add((x, y))
        x += dx
        y += dy
      x, y = x1, y1
      while x in range(m) and y in range(n):
        res.add((x, y))
        x -= dx
        y -= dy
      all_nodes |= res

  return sum(int(x in range(m) and y in range(n)) for x, y in all_nodes)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))