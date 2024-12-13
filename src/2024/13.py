from pathlib import Path
from .. import utils as u
from rich import print

import regex as re

def sln1(input):
  ans = 0
  chunks = re.split(r'\n\n', input)
  for chunk in chunks:
    ai, aj, bi, bj, ti, tj = map(int, re.findall(r'\d+', chunk))
    det = ai * bj - aj * bi
    if det == 0:
      continue
    a_presses = round((bj * ti - bi * tj) / det)
    b_presses = round((ai * tj - aj * ti) / det)
    if a_presses*ai + b_presses*bi == ti and a_presses*aj + b_presses*bj == tj:
      ans += a_presses*3 + b_presses
  return ans

def sln2(input):
  ans = 0
  chunks = re.split(r'\n\n', input)
  for chunk in chunks:
    ai, aj, bi, bj, ti, tj = map(int, re.findall(r'\d+', chunk))
    ti += 10000000000000
    tj += 10000000000000
    det = ai * bj - aj * bi
    if det == 0:
      continue
    a_presses = round((bj * ti - bi * tj) / det)
    b_presses = round((ai * tj - aj * ti) / det)
    if a_presses*ai + b_presses*bi == ti and a_presses*aj + b_presses*bj == tj:
      ans += a_presses*3 + b_presses
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))