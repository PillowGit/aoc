from pathlib import Path
from .. import utils as u
from rich import print

import regex as re
from collections import deque

M, N = 101, 103
mid_m = M // 2
mid_n = N // 2

def sln1(input):
  moves = 100
  quads = [0] * 4
  for line in input:
    x, y, dx, dy = map(int, re.findall(r'-?\d+', line))
    x = (x + dx * moves) % M
    y = (y + dy * moves) % N
    if x == mid_m or y == mid_n:
      continue
    quad = -1
    if x in range(mid_m) and y in range(mid_n):
      quad = 0
    elif x in range(mid_m + 1, M) and y in range(mid_n):
      quad = 1
    elif x in range(mid_m) and y in range(mid_n + 1, N):
      quad = 2
    else:
      quad = 3
    quads[quad] += 1
  return quads[0] * quads[1] * quads[2] * quads[3]

def hastree(grid):
  def dfs(i, j):
    q = deque()
    q.append((i, j))
    seen = set()
    seen.add((i, j))
    while q:
      i, j = q.popleft()
      for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = i + dx, j + dy
        if (ni, nj) in seen:
          continue
        if ni not in range(M) or nj not in range(N):
          continue
        if grid[ni][nj] == '#':
          q.append((ni, nj))
          seen.add((ni, nj))
    return len(seen)
  for i in range(len(grid)):
    for j in range(len(grid[0])):
      if grid[i][j] == '#':
        if dfs(i, j) >= 15:
          return True

def sln2(input):
  bots = [[int(x) for x in re.findall(r'-?\d+', line)] for line in input]
  seconds = 0
  while True:
    seconds += 1
    grid = [['.' for _ in range(N)] for _ in range(M)]
    for i in range(len(bots)):
      x, y, dx, dy = bots[i]
      x = (x + dx) % M
      y = (y + dy) % N
      bots[i] = [x, y, dx, dy]
      grid[x][y] = '#'
    if hastree(grid):
      return seconds

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))