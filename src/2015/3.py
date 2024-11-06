from pathlib import Path
from .. import utils as u

def sln1(input):
  x,y = 0,0
  seen = set()
  for c in input:
    seen.add((x,y))
    if c == '^': y += 1
    elif c == 'v': y -= 1
    elif c == '<': x -= 1
    elif c == '>': x += 1
  seen.add((x,y))
  return len(seen)

def sln2(input):
  s1,s2 = 0,0
  r1,r2 = 0,0
  seen = set()
  def update():
    seen.add((s1,r1))
    seen.add((s2,r2))
  for i,c in enumerate(input):
    update()
    if i % 2 == 0:
      x,y = s1,r1
    else:
      x,y = s2,r2
    if c == '^': y += 1
    elif c == 'v': y -= 1
    elif c == '<': x -= 1
    elif c == '>': x += 1
    if i % 2 == 0:
      s1,r1 = x,y
    else:
      s2,r2 = x,y
  update()
  return len(seen)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))