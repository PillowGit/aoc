from pathlib import Path
from .. import utils as u
from rich import print

import regex as re

def sln1(input):
  # Parsing
  input_ints = list(map(int, re.findall(r'\d+', input)))
  A, B, C = input_ints[:3]
  instructions = input_ints[3:]
  # Simulation function
  outputs = []
  def sim(idx):
    # Get the instruction and operand
    nonlocal A, B, C, outputs
    instruction = instructions[idx]
    operand = instructions[idx + 1] if idx + 1 < len(instructions) else Exception('What the fuck')
    # Calculate the combo value
    assert isinstance(operand, int) and operand in range(8)
    if operand in (0, 1, 2, 3):
      combo = int(operand)
    elif operand == 4:
      combo = A
    elif operand == 5:
      combo = B
    elif operand == 6:
      combo = C
    elif operand == 7:
      combo = Exception('What the fuck')
    # Run the instruction
    match instruction:
      case 0:
        A = A//(2**combo)
        return None
      case 1:
        B = B ^ int(operand)
        return None
      case 2:
        B = combo % 8
        return None
      case 3:
        if A == 0:
          return None
        else:
          return int(operand)
      case 4:
        B = B ^ C
        return None
      case 5:
        outputs.append(combo % 8)
        return None
      case 6:
        B = A//(2**combo)
        return None
      case 7:
        C = A//(2**combo)
        return None
      case _:
        raise Exception('What the fuck')
  # Simulate
  i = 0 
  while i < len(instructions):
    result = sim(i)
    if isinstance(result, int):
      i = result
    else:
      i += 2
  return ','.join(map(str, outputs))

def sln2(input):
  # Parsing
  instructions = list(map(int, re.findall(r'\d+', input)))[3:]
  target = instructions[::-1]
  def dfs(a, ind):
    nonlocal target, instructions
    if ind == len(target): return a
    for i in range(8):
      input_nums = [a*8+i, 0, 0] + instructions
      input_str = ','.join(map(str, input_nums))
      output = list(map(int, sln1(input_str).split(',')))
      if output and output[0] == target[ind]:
        if result := dfs((a*8+i), ind+1):
          return result
  return dfs(0, 0)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))