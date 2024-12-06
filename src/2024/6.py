from pathlib import Path
from rich import print
from .. import utils as u
import copy
from collections import defaultdict
from alive_progress import alive_bar

dirs = {
  '^': (-1, 0),
  'v': (1, 0),
  '>': (0, 1),
  '<': (0, -1)
}
faces = ['^', '>', 'v', '<']
def pgrid(input):
  for row in input:
    print(' '.join(row))

def sln1(input):
  # find guard
  start = None
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] == '^':
        start = (i, j)
        break
  # simulate until guard leaves
  x, y = start
  while x in range(len(input)) and y in range(len(input)):
    movement = dirs[input[x][y]]
    xx = x + movement[0]
    yy = y + movement[1]
    try:
      if input[xx][yy] == '#':
        input[x][y] = faces[(faces.index(input[x][y]) + 1) % 4]
        continue
    except Exception:
      ...
    tmp = input[x][y]
    input[x][y] = 'X'
    x, y = xx, yy
    try:
      input[x][y] = tmp
    except Exception:
      ...
  # pgrid(input)
  return sum([row.count('X') for row in input])

def sim_cycle(input, start):
  cur_face = '^'
  x, y = start
  seen = set()
  while x in range(len(input)) and y in range(len(input[0])):
    if (x, y, cur_face) in seen:
      return True
    seen.add((x, y, cur_face))
    movement = dirs[cur_face]
    xx = x + movement[0]
    yy = y + movement[1]
    if xx in range(len(input)) and yy in range(len(input[0])):
      if input[xx][yy] == '#':
        cur_face = faces[(faces.index(cur_face) + 1) % 4]
        continue
    input[x][y] = 'X'
    x, y = xx, yy
  return False

def sln2(input):
  # Fills out X's
  grid = copy.deepcopy(input)
  sln1(grid)
  # Find start
  start = (-1, -1)
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] == '^':
        input[i][j] = '.'
        start = (i, j)
        break
  # simulate each X as an obstacle, check cycles
  ans = 0
  with alive_bar(len(input) * len(input[0])) as bar:
    for i in range(len(input)):
      for j in range(len(input[0])):
        if grid[i][j] == 'X':
          newgrid = copy.deepcopy(input)
          newgrid[i][j] = '#'
          if sim_cycle(newgrid, start):
            ans += 1
        bar()
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(copy.deepcopy(parsed_input)))
  print('Part 2:', sln2(copy.deepcopy(parsed_input)))