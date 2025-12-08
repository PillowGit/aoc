import math
from pathlib import Path
from .. import utils as u
from rich import print

class uf:
  def __init__(self, n):
    self.parent = list(range(n))
    self.size = [1] * n
  def find(self, i):
    if self.parent[i] == i:
      return i
    self.parent[i] = self.find(self.parent[i])
    return self.parent[i]
  def union(self, i, j):
    ri = self.find(i)
    rj = self.find(j)
    if ri != rj:
      if self.size[ri] < self.size[rj]:
        ri, rj = rj, ri
      self.parent[rj] = ri
      self.size[ri] += self.size[rj]
      return True
    return False
def dist(a, b):
  return math.sqrt(sum((x-y)**2 for x, y in zip(a, b)))

def sln1(positions):
  edges = []
  for i in range(len(positions)):
    for j in range(i+1, len(positions)):
      edges.append((dist(positions[i], positions[j]), i, j))
  edges.sort()
  u = uf(len(positions))
  for i in range(1000):
    _, a, b = edges[i]
    u.union(a, b)
  sizes = []
  for i in range(len(positions)):
    if u.find(i) == i:
      sizes.append(u.size[i])
  sizes.sort(reverse=True)
  top3 = sizes[:3]
  return math.prod(top3)

def sln2(positions):
  edges = []
  for i in range(len(positions)):
    for j in range(i+1, len(positions)):
      edges.append((dist(positions[i], positions[j]), i, j))
  edges.sort()
  u = uf(len(positions))
  last2 = []
  for _, i, j in edges:
    if u.union(i, j):
      last2 = [i, j]
  return positions[last2[0]][0] * positions[last2[1]][0]

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [tuple(int(x) for x in line.split(',')) for line in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))