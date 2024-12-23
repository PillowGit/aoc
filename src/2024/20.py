from pathlib import Path
from .. import utils as u
from rich import print

from collections import defaultdict

# 6854 (too high)
def sln1(input):
  start, end = None, None
  for r in range(len(input)):
    for c in range(len(input[r])):
      if input[r][c] == 'S':
        start = (r, c)
      elif input[r][c] == 'E':
        end = (r, c)
  path, indices = [], {}
  q = [(start, 0)]
  while q:
    (i, j), ind = q.pop()
    indices[(i, j)] = ind
    path.append((i, j))
    if (i, j) == end:
      break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ni, nj = i + di, j + dj
      if ni not in range(len(input)) or nj not in range(len(input[ni])):
        continue
      if input[ni][nj] == '#':
        continue
      if (ni, nj) in indices:
        continue
      q.append(((ni, nj), ind + 1))
  
  seconds = len(path) - 1
  saved_seconds = defaultdict(int)
  for i, j in path:
    idx = indices[(i, j)]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ni, nj = i + di, j + dj
      if ni not in range(len(input)) or nj not in range(len(input[ni])):
        continue
      if input[ni][nj] == '.':
        continue
      ii, jj = ni + di, nj + dj
      if ii not in range(len(input)) or jj not in range(len(input[ii])):
        continue
      if input[ii][jj] == '#':
        continue
      if (ii, jj) not in indices:
        continue
      end_idx = indices[(ii, jj)]
      if end_idx < idx:
        continue
      cheat_seconds = (idx + 1) + 1 + (seconds - end_idx)
      saved = seconds - cheat_seconds
      saved_seconds[saved] += 1
  ans = 0
  for k, v in saved_seconds.items():
    if k >= 100:
      ans += v
  return ans
    

def sln2(input):
  start, end = None, None
  for r in range(len(input)):
    for c in range(len(input[r])):
      if input[r][c] == 'S':
        start = (r, c)
      elif input[r][c] == 'E':
        end = (r, c)
  path, indices = [], {}
  q = [(start, 0)]
  while q:
    (i, j), ind = q.pop()
    indices[(i, j)] = ind
    path.append((i, j))
    if (i, j) == end:
      break
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ni, nj = i + di, j + dj
      if ni not in range(len(input)) or nj not in range(len(input[ni])):
        continue
      if input[ni][nj] == '#':
        continue
      if (ni, nj) in indices:
        continue
      q.append(((ni, nj), ind + 1))
  
  seconds = len(path) - 1
  ans = 0
  for i in range(seconds):
    for j in range(i+1, len(path)):
      a, b = path[i], path[j]
      dist = abs(a[0] - b[0]) + abs(a[1] - b[1])
      if dist > 20:
        continue
      cheat = (i + 1) + dist + (seconds - j - 1)
      saved = (seconds - cheat)
      if saved >= 100:
        ans += 1
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))