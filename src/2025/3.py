from pathlib import Path
from .. import utils as u
from rich import print

def sln1(input):
  ans = 0
  for line in input:
    lmax = max(line[:-1])
    lmaxind = line.index(lmax)
    rmax = max(line[lmaxind+1:])
    ans += int(f'{lmax}{rmax}')
  return ans

def sln2(input):
  ans = 0
  for line in input:
    n, k = len(line), 12
    final = []
    start = 0
    for i in range(k):
      r = k - i
      end = n - r + 1
      maxdigit, maxind = -1, -1
      for j in range(start, end):
        digit = line[j]
        if digit > maxdigit:
          maxdigit = digit
          maxind = j
      final.append(maxdigit)
      start = maxind + 1
    ans += int(''.join(map(str, final)))
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [[int(c) for c in x] for x in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))