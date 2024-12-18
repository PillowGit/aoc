from pathlib import Path
from .. import utils as u
from rich import print

import regex as re
from collections import deque
from copy import deepcopy

M,N = 71,71
pop_amnt = 1024
#M,N = 7,7 # test input
#pop_amnt = 12

def show(grid):
  for row in grid:
    print(''.join(row))
  print()

# 140
def sln1(input):
  # Build grid
  grid = [['.' for _ in range(N)] for _ in range(M)]
  for i, line in enumerate(input):
    x, y = map(int, re.findall(r'\d+', line))
    grid[y][x] = '#'
    if i == pop_amnt - 1: break
  # Bfs
  q = deque([(0, 0, 0)])
  while q:
    steps, x, y = q.popleft()
    if x == M-1 and y == N-1:
      return steps
    for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
      nx, ny = x+dx, y+dy
      if nx in range(M) and ny in range(N) and grid[nx][ny] == '.':
        grid[nx][ny] = '#'
        q.append((steps+1, nx, ny))

# 2991
def sln2(input):
  # Make grid
  grid = [['.' for _ in range(N)] for _ in range(M)]
  input = deque(input)
  def add_next_line():
    x, y = map(int, re.findall(r'\d+', input.popleft()))
    grid[y][x] = '#'
    return (x,y)
  for _ in range(pop_amnt): add_next_line()
  # Define bfs
  def bfs():
    nonlocal grid
    old_grid = deepcopy(grid)
    q = deque([(0, 0, 0)])
    while q:
      steps, x, y = q.popleft()
      if x == M-1 and y == N-1:
        grid = old_grid
        return steps
      for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy
        if nx in range(M) and ny in range(N) and grid[nx][ny] == '.':
          grid[nx][ny] = '#'
          q.append((steps+1, nx, ny))
    grid = old_grid
    return -1
  # Simulate
  i = pop_amnt
  last = None
  while True:
    res = bfs()
    if res == -1: return f'{last[0]},{last[1]}'
    i += 1
    last = add_next_line()

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))