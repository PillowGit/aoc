from pathlib import Path
from .. import utils as u

def sln1(input):
  ans = 0
  for i in range(1, len(input)):
    l, r = input[i-1], input[i]
    if int(l) <= int(r):
      ans += 1
  return ans

def sln2(input):
  last = 0
  ans = 0
  for i in range(3, len(input)):
    l, m, r = input[i-3:i]
    s = int(l) + int(m) + int(r)
    if s > last:
      ans += 1
    last = s
  return ans - 1

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))