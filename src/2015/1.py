from pathlib import Path
from .. import utils as u

def sln1(input):
  return input.count('(') - input.count(')')

def sln2(input):
  for i, c in enumerate(input):
    if input[:i].count('(') - input[:i].count(')') < 0:
      return i

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))