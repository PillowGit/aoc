from pathlib import Path
from .. import utils as u
from collections import Counter

def sln1(input):
  l, r = [], []
  for line in input:
    left, right = line.split('   ')
    l.append(int(left))
    r.append(int(right))
  l.sort()
  r.sort()
  ans = 0
  for a,b in zip(l, r):
    ans += abs(a-b)
  return ans

def sln2(input):
  l, r = [], []
  for line in input:
    left, right = line.split('   ')
    l.append(int(left))
    r.append(int(right))
  r = Counter(r)
  ans = 0
  for x in l:
    ans += r[x] * x
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))