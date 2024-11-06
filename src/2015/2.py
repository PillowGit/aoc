from pathlib import Path
from .. import utils as u

def sln1(input):
  total = 0
  for l, w, h in input:
    l, w, h = int(l), int(w), int(h)
    sides = [l*w, w*h, h*l]
    total += 2*sum(sides) + min(sides)
  return total

def sln2(input):
  total = 0
  for l, w, h in input:
    l, w, h = int(l), int(w), int(h)
    total += l*w*h + 2*(l+w+h-max(l, w, h))
  return total

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [x.split('x') for x in u.parsing.lines(input_file)]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))