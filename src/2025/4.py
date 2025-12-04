from pathlib import Path
from .. import utils as u
from rich import print

def iterate(input, part2=False):
  removed = 0
  n, m = len(input), len(input[0])
  dirs = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for r in range(n):
    for c in range(m):
      if input[r][c] == '@':
        adj = 0
        for dr, dc in dirs:
          nr, nc = r + dr, c + dc
          if nr in range(n) and nc in range(m) and input[nr][nc] == '@':
            adj += 1
        if adj < 4:
          removed += 1
          if part2: input[r][c] = '.'
  return removed

def sln1(input):
  return iterate(input)

def sln2(input):
  ans = 0
  while True:
    removed = iterate(input, True)
    if removed == 0:
      break
    ans += removed
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [list(line) for line in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))