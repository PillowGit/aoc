from pathlib import Path
from .. import utils as u
from rich import print

from collections import deque
import numpy as np
from copy import deepcopy
from shapely.geometry import Polygon

def mark_region(grid, x, y, region):
  m, n = len(grid), len(grid[0])
  perimeter = 0
  q = deque([(x, y)])
  seen = set()
  seen.add((x, y))
  while q:
    i, j = q.popleft()
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ni, nj = i + dx, j + dy
      if (ni, nj) in seen:
        continue
      if ni not in range(m) or nj not in range(n):
        perimeter += 1
        continue
      if grid[ni][nj] != region:
        perimeter += 1
        continue
      q.append((ni, nj))
      seen.add((ni, nj))
  for i, j in seen:
    grid[i][j] = '.'
  return len(seen), perimeter

def pp(grid):
  for row in grid:
    print(''.join(row))
  print()

# Wrong:
# 1444709
def sln1(input):
  ans = 0
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] != '.':
        ret = mark_region(input, i, j, input[i][j])
        ans += ret[0] * ret[1]
  return ans

def get_num_sides(grid, edges):
  m, n = len(grid), len(grid[0])
  # Split each cell up into 2x2 squares so it fits a nice polygon with shapely
  new_edges = []
  for i, j in edges:
    pts = set([(i*2, j*2), (i*2+1, j*2), (i*2, j*2+1), (i*2+1, j*2+1)])
    # Up, right, down, left, in that order
    shape_edges = [True] * 4
    for i, (dx, dy) in enumerate([(-1, 0), (0, 1), (1, 0), (0, -1)]):
      ni, nj = i + dx, j + dy
      if ni in range(m) and nj in range(n) and grid[ni][nj] == '.':
        shape_edges[i] = False
    # Look at perimeter edges of the cell to determine the new edges, '.' means its part of the shape, out of range or != '.' means its not part of the shape
    if not shape_edges[0] and not shape_edges[1]:
      pts.remove((i*2, j*2+1))
    if not shape_edges[1] and not shape_edges[2]:
      pts.remove((i*2+1, j*2+1))
    if not shape_edges[2] and not shape_edges[3]:
      pts.remove((i*2+1, j*2))
    if not shape_edges[3] and not shape_edges[0]:
      pts.remove((i*2, j*2))
    new_edges.extend(list(pts))
  centroid = np.mean(new_edges, axis=0)
  def angle_w_centroid(p):
    vector = np.array(p) - centroid
    return np.arctan2(vector[1], vector[0])
  sorted_edges = sorted(new_edges, key=angle_w_centroid)
  out = '['
  for i, j in sorted_edges:
    out += f'({i},{j}),'
  out = out[:-1] + ']'
  print(out)
  poly = Polygon(sorted_edges)
  # Return the number of sides of the polygon
  return -1

def get_cost(grid, x, y, region):
  m, n = len(grid), len(grid[0])
  q = deque([(x, y)])
  seen = set()
  seen.add((x, y))
  polygon_edges = set()
  while q:
    i, j = q.popleft()
    perimeter = 0
    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
      ni, nj = i + dx, j + dy
      if (ni, nj) in seen:
        continue
      if ni not in range(m) or nj not in range(n):
        perimeter += 1
        continue
      if grid[ni][nj] != region:
        perimeter += 1
        continue
      q.append((ni, nj))
      seen.add((ni, nj))
    if perimeter > 0:
      polygon_edges.add((i, j))
  for i, j in seen:
    grid[i][j] = '.'
  return len(seen) * get_num_sides(grid, list(polygon_edges))

# Wrong:
# 724773
# 3674340
def sln2(input):
  ans = 0
  for i in range(len(input)):
    for j in range(len(input[0])):
      if input[i][j] != '.':
        reg = input[i][j]
        cost = get_cost(input, i, j, input[i][j])
        print(f'{reg}: {cost}')
        ans += cost
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(deepcopy(parsed_input)))
  print('Part 2:', sln2(deepcopy(parsed_input)))