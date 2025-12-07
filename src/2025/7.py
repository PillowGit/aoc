from collections import deque
from pathlib import Path
from .. import utils as u
from rich import print

def printgrid(g):
  print('\n'.join(''.join(row) for row in g))

def sln1(input):
  ans = 0
  g = input
  lasers = set()
  lasers.add(g[0].index('S'))
  depth = 1
  while depth < len(g):
    new_lasers = set()
    for l in lasers:
      if g[depth][l] == '^':
        lft, rgt = l - 1, l + 1
        if lft in range(len(g[depth])):
          new_lasers.add(lft)
        if rgt in range(len(g[depth])):
          new_lasers.add(rgt)
        ans += 1
      else:
        new_lasers.add(l)
    lasers = new_lasers
    # print(''.join('|' if i in lasers else g[depth][i] for i in range(len(g[depth]))))
    depth += 1
  return ans

def sln2(input):
  g = input
  g.append(['.'] * len(g[0]))
  lasers = [0] * len(g[0])
  lasers[g[0].index('S')] = 1
  depth = 1
  while depth < len(g):
    new_lasers = [0] * len(g[depth])
    for l in range(len(g[depth])):
      if lasers[l] > 0:
        if g[depth][l] == '^':
          lft, rgt = l - 1, l + 1
          if lft in range(len(g[depth])):
            new_lasers[lft] += lasers[l]
          if rgt in range(len(g[depth])):
            new_lasers[rgt] += lasers[l]
        else:
          new_lasers[l] += lasers[l]
    lasers = new_lasers
    depth += 1
  return sum(lasers)


if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [list(l.strip()) for l in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))