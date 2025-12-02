from pathlib import Path
from .. import utils as u
from rich import print

def sln1(input):
  start = 50
  ans = 0
  for line in input:
    start += line
    start %= 100
    if start == 0:
      ans += 1
  return ans

#6936 too high
def sln2(input):
  start = 50
  ans = 0
  for line in input:
    prev = start
    while abs(line) > 99:
      if line > 0:
        line -= 100
      else:
        line += 100
      ans += 1
    start += line
    if prev != 0 and (start < 0 or start > 99 or start == 0):
      ans += 1
    start %= 100
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [(-1 * int(line[1:]) if line[0] == 'L' else int(line[1:])) for line in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))