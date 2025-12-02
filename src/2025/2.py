from pathlib import Path
from .. import utils as u
from rich import print

# --------------- pt 1

def invalid(x):
  if len(x) % 2 != 0:
    return False
  n = len(x) // 2
  return x[:n] == x[n:]

def sln1(input):
  ans = 0
  for start, end in input:
    for x in range(int(start), int(end) + 1):
      if invalid(str(x)):
        ans += x
  return ans

# --------------- pt 2

def invalid_again(x):
  for i in range(0, len(x) // 2 + 1):
    s = x[0:i]
    for n in range(1, 10): # check repeats up to 5x, max len of any string in input is 10 digits
      if s * n == x[i:]:
        return True
  return False

def sln2(input):
  ans = 0
  for start, end in input:
    for x in range(int(start), int(end) + 1):
      if invalid_again(str(x)):
        ans += x
  return ans


if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [x.split('-') for x in open(input_file).read().strip().split(',')]


  # max_str_len = 0
  # for start, end in parsed_input:
  #   max_str_len = max(max_str_len, len(start), len(end))
  # print(max_str_len)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))