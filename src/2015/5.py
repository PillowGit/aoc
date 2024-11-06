from pathlib import Path
from .. import utils as u

def sln1(input):
  def check_str(s):
    vowels = 'aeiou'
    bad = ['ab', 'cd', 'pq', 'xy']
    if any(b in s for b in bad):
      return False
    if sum(c in vowels for c in s) < 3:
      return False
    for i in range(len(s) - 1):
      if s[i] == s[i + 1]:
        return True
    return False
  return sum(check_str(s) for s in input)


def sln2(input):
  def check_str(s):
    for i in range(len(s) - 2):
      if s[i] == s[i + 2]:
        break
    else:
      return False
    for i in range(len(s) - 3):
      if s[i:i+2] in s[i+2:]:
        return True
    return False
  return sum(check_str(s) for s in input)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))