from pathlib import Path
from .. import utils as u
from rich import print
import re

def sln1(input):
  pattern = r"(\d+|[^\s\d])"
  results = re.findall(pattern, input.strip())
  d, s = ([x for x in results if x.isdigit()], [x for x in results if x in '+*'])
  ans = [[0 if x == '+' else 1, x] for x in s]
  for i, x in enumerate(d):
    ii = i % len(ans)
    if ans[ii][1] == '+':
      ans[ii][0] += int(x)
    elif ans[ii][1] == '*':
      ans[ii][0] *= int(x)
  return sum(x[0] for x in ans)

def sln2(input):
  g = [list(l) for l in input.split('\n')]
  w = max(len(row) for row in g)
  for r in g:
    if len(r) < w: r.extend([' '] * (w - len(r)))
  g = [list(row) for row in zip(*g)]
  g = [''.join(row).rstrip() for row in g]
  ans, curr, op = 0, 0, None
  for line in g:
    if line == '':
      op = None
      ans += curr
      curr = 0
      continue
    line = line.strip()
    if line[-1] in '+*':
      op = line[-1]
      line = line[:-1]
    n = int(line)
    if op == '+':
      curr += n
    else:
      if curr == 0: curr = 1
      curr *= n
  return ans + curr

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = open(input_file).read()

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))