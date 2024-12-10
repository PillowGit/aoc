from pathlib import Path
from .. import utils as u
from rich import print

from collections import deque

def find_9s(grid, i, j):
  m, n = len(grid), len(grid[0])
  q = deque()
  q.append((i, j))
  res = set()
  while q:
    x, y = q.popleft()
    v = int(grid[x][y])
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      a, b = x + dx, y + dy
      if a not in range(m) or b not in range(n):
        continue
      ov = int(grid[a][b])
      if ov-v != 1:
        continue
      if ov == 9:
        res.add((a, b))
      else:
        q.append((a, b))
  return res

def sln1(input):
  ans = 0
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] == '0':
        ans += len(find_9s(input, i, j))
  return ans

def find_ways(grid, i, j):
  m, n = len(grid), len(grid[0])
  q = deque()
  q.append((i, j))
  res = 0
  while q:
    x, y = q.popleft()
    v = int(grid[x][y])
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
      a, b = x + dx, y + dy
      if a not in range(m) or b not in range(n):
        continue
      ov = int(grid[a][b])
      if ov-v != 1:
        continue
      if ov == 9:
        res += 1
      else:
        q.append((a, b))
  return res

def sln2(input):
  ans = 0
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] == '0':
        ans += find_ways(input, i, j)
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))