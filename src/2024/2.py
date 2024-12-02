from pathlib import Path
from .. import utils as u

def check(l):
  if sorted(l) != l and sorted(l, reverse=True) != l:
    return False
  passing = True
  for i in range(1, len(l)):
    if abs(l[i] - l[i-1]) not in range(1, 4):
      passing = False
      break
  return passing

def sln1(input):
  return sum(int(check([int(x) for x in l.split()])) for l in input)

def sln2(input):
  return sum((lambda l:int(any(check(t) for t in ([l] + [l[:i]+l[i+1:] for i in range(len(l))]))))([int(x) for x in l.split()]) for l in input)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))