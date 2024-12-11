from pathlib import Path
from .. import utils as u
from rich import print
from collections import defaultdict

# Wrong:
# 868621
def sln1(input):
  BLINKS = 25
  stones = [int(x) for x in input]
  for _ in range(BLINKS):
    new_stones = []
    for stone in stones:
      if stone == 0:
        new_stones.append(1)
      elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        left_half = stone[:len(stone) // 2]
        right_half = stone[len(stone) // 2:]
        new_stones.append(int(left_half))
        new_stones.append(int(right_half))
      else:
        new_stones.append(stone * 2024)
    stones = new_stones
  return len(stones)


def sln2(input):
  BLINKS = 75
  stones = defaultdict(int)
  for x in input:
    stones[int(x)] += 1
  for _ in range(BLINKS):
    new_stones = defaultdict(int)
    for stone in stones:
      if stone == 0:
        new_stones[1] += stones[stone]
      elif len(str(stone)) % 2 == 0:
        stone = str(stone)
        left_half = stone[:len(stone) // 2]
        right_half = stone[len(stone) // 2:]
        new_stones[int(left_half)] += stones[int(stone)]
        new_stones[int(right_half)] += stones[int(stone)]
      else:
        new_stones[stone * 2024] += stones[stone]
    stones = new_stones
  return sum(stones.values())

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.read(input_file).split()

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))