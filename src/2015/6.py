from pathlib import Path
from .. import utils as u

def sln1(input):
  grid = [[False for i in range(1000)] for j in range(1000)]
  def doaction(action, i, j):
    if action[0] == 'toggle':
      grid[i][j] = not grid[i][j]
    if action[1] == 'on':
      grid[i][j] = True
    if action[1] == 'off':
      grid[i][j] = False
  for line in input:
    line = line.split(' ')
    action = [line[0], line[1]]
    start = line[-3].split(',')
    end = line[-1].split(',')
    for i in range(int(start[0]), int(end[0]) + 1):
      for j in range(int(start[1]), int(end[1]) + 1):
        doaction(action, i, j)
  return sum([sum(row) for row in grid])

def sln2(input):
  grid = [[0 for i in range(1000)] for j in range(1000)]
  def doaction(action, i, j):
    if action[0] == 'toggle':
      grid[i][j] += 2
    if action[1] == 'on':
      grid[i][j] += 1
    if action[1] == 'off':
      grid[i][j] = max(0, grid[i][j] - 1)
  for line in input:
    line = line.split(' ')
    action = [line[0], line[1]]
    start = line[-3].split(',')
    end = line[-1].split(',')
    for i in range(int(start[0]), int(end[0]) + 1):
      for j in range(int(start[1]), int(end[1]) + 1):
        doaction(action, i, j)
  return sum([sum(row) for row in grid])

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))