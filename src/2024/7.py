from pathlib import Path
from rich import print
from collections import deque
from .. import utils as u

# Wrong:
# 540145481
def sln1(input):
  ans = 0
  data = []
  for line in input:
    dat = line.split(':')
    dat[0] = int(dat[0])
    dat[1] = deque(map(int, dat[1].strip().split()))
    data.append(dat)
  for target, nums in data:
    evals = []
    evals.append(str(nums.popleft()))
    while nums:
      new_evals = []
      next_num = nums.popleft()
      for ev in evals:
        new_evals.append(f'({ev})+{next_num}')
        new_evals.append(f'({ev})*{next_num}')
      evals = new_evals
    if target in map(eval, evals):
      ans += target
  return ans

def sln2(input):
  ans = 0
  data = []
  for line in input:
    dat = line.split(':')
    dat[0] = int(dat[0])
    dat[1] = deque(map(int, dat[1].strip().split()))
    data.append(dat)
  for target, nums in data:
    evals = []
    evals.append(str(nums.popleft()))
    while nums:
      new_evals = []
      next_num = nums.popleft()
      for ev in evals:
        new_evals.append(f'({ev})+{next_num}')
        new_evals.append(f'({ev})*{next_num}')
        new_evals.append(f'int(str({ev})+str({next_num}))')
      evals = new_evals
    if target in map(eval, evals):
      ans += target
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))