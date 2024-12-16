from pathlib import Path
from .. import utils as u
from rich import print

import heapq as hq

def sln1(grid):
  DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
  m, n = len(grid), len(grid[0])
  si, sj = None, None
  ei, ej = None, None
  for i in range(m):
    for j in range(n):
      if grid[i][j] == 'S':
        si, sj = i, j
      if grid[i][j] == 'E':
        ei, ej = i, j
  pq = []
  seen = set()
  hq.heappush(pq, (0, si, sj, 1))
  dists = {}
  best = None
  while pq:
    cost, i, j, direction = hq.heappop(pq)
    if (i, j, direction) not in dists:
      dists[(i, j, direction)] = cost
    if i == ei and j == ej and best is None:
      best = cost
    if (i, j, direction) in seen:
      continue
    seen.add((i, j, direction))
    di, dj = DIRS[direction]
    ii, jj = i + di, j + dj
    if ii in range(m) and jj in range(n) and grid[ii][jj] != '#':
      hq.heappush(pq, (cost + 1, ii, jj, direction))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 1) % 4))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 3) % 4))
  return best

def sln2(grid):
  DIRS = [(-1,0),(0,1),(1,0),(0,-1)]
  m, n = len(grid), len(grid[0])
  si, sj = None, None
  ei, ej = None, None
  for i in range(m):
    for j in range(n):
      if grid[i][j] == 'S':
        si, sj = i, j
      if grid[i][j] == 'E':
        ei, ej = i, j

  pq = []
  seen = set()
  hq.heappush(pq, (0, si, sj, 1))
  dists = {}
  best = None
  while pq:
    cost, i, j, direction = hq.heappop(pq)
    if (i, j, direction) not in dists:
      dists[(i, j, direction)] = cost
    if i == ei and j == ej and best is None:
      best = cost
    if (i, j, direction) in seen:
      continue
    seen.add((i, j, direction))
    di, dj = DIRS[direction]
    ii, jj = i + di, j + dj
    if ii in range(m) and jj in range(n) and grid[ii][jj] != '#':
      hq.heappush(pq, (cost + 1, ii, jj, direction))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 1) % 4))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 3) % 4))

  pq = []
  seen = set()
  for direction in range(4):
    hq.heappush(pq, (0, ei, ej, direction))
  bdists = {}
  while pq:
    cost, i, j, direction = hq.heappop(pq)
    if (i, j, direction) not in bdists:
      bdists[(i, j, direction)] = cost
    if (i, j, direction) in seen:
      continue
    seen.add((i, j, direction))
    di, dj = DIRS[(direction + 2) % 4]
    ii, jj = i + di, j + dj
    if ii in range(m) and jj in range(n) and grid[ii][jj] != '#':
      hq.heappush(pq, (cost + 1, ii, jj, direction))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 1) % 4))
    hq.heappush(pq, (cost + 1000, i, j, (direction + 3) % 4))
  ans = set()
  for i in range(m):
    for j in range(n):
      for direction in range(4):
        if (i, j, direction) in dists and (i, j, direction) in bdists and dists[(i, j, direction)] + bdists[(i, j, direction)] == best:
          ans.add((i, j))
  return len(ans)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))