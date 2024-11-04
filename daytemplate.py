from pathlib import Path
from .. import utils as u

def sln1(input):
  return 1

def sln2(input):
  return 2

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = input_file.read_text().strip()

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))