from pathlib import Path
from .. import utils as u
import regex as re

def sln1(input):
  ans = 0
  text = ''.join(input)
  pattern = r"mul\(\d{1,3},\d{1,3}\)"
  matches = re.findall(pattern, text)
  for match in matches:
    nums = match[:-1].split('(')[1].split(',')
    ans += int(nums[0]) * int(nums[1])
  return ans

def sln2(input):
  ans = 0
  text = ''.join(input)
  pattern = r"(mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\))"
  matches = re.findall(pattern, text)
  doing = True
  for match in matches:
    if match == "do()":
      doing = True
    elif match == "don't()":
      doing = False
    elif doing:
      nums = match[:-1].split('(')[1].split(',')
      ans += int(nums[0]) * int(nums[1])
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))