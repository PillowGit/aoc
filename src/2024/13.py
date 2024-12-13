from pathlib import Path
from .. import utils as u
from rich import print

from sys import setrecursionlimit
setrecursionlimit(10**6)

def sln1(input):
  ans = 0
  button_a_movement = 0
  button_b_movement = 0
  button_location = 0
  parse_step = 0
  # Solving
  def solve_claw_machine(x, y):
  # Parsing
  def getints(string):
      coords = string.replace(' ','').split(':')[1].split(',')
      return (int(coords[0][2:]), int(coords[1][2:]))
  for line in input:
    if parse_step == 0:
      button_a_movement = getints(line)
    elif parse_step == 1:
      button_b_movement = getints(line)
    elif parse_step == 2:
      button_location = getints(line)
    else:
      ans += solve_claw_machine(0, 0)
      parse_step = -1
    parse_step += 1
  return ans

def sln2(input):
  return -1

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))