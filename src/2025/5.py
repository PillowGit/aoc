from pathlib import Path
from .. import utils as u
from rich import print

def sln1(input):
  ranges, ids = input
  ans = 0
  for n in ids:
    for r in ranges:
      if n in range(r[0], r[1]+1):
        ans += 1
        break
  return ans

def sln2(input):
  ranges, _ = input
  ranges.sort()
  merged = [ranges[0]]
  for i in range(1, len(ranges)):
    r = ranges[i]
    if r[0] <= merged[-1][1] + 1:
      merged[-1] = (merged[-1][0], max(merged[-1][1], r[1]))
    else:
      merged.append(r)
  ans = 0
  for r in merged:
    ans += r[1] - r[0] + 1
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  ranges, ids = open(input_file).read().strip().split('\n\n')
  ranges = [tuple(map(int, line.split('-'))) for line in ranges.strip().split('\n')]
  ids = list(map(int, ids.strip().split('\n')))
  parsed_input = (ranges, ids)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))