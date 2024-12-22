from pathlib import Path
from .. import utils as u
from rich import print

from functools import cache

towels = ['w', 'u', 'b', 'r', 'g']
class Trie:
  def __init__(self):
    self.children = [None] * 5
    self.end = False
def add(root, word):
  curr = root
  for c in word:
    i = towels.index(c)
    if curr.children[i] is None:
      new = Trie()
      curr.children[i] = new
    curr = curr.children[i]
  curr.end = True
@cache
def count(root, word):
  curr = root
  n = len(word)
  combos = 0
  if n == 0: return 1
  for i in range(n):
    next_letter = towels.index(word[i])
    if curr.children[next_letter] is None:
      return combos
    else:
      curr = curr.children[next_letter]
      if curr.end:
        combos += count(root, word[i+1:])
  return combos

def sln1(input):
  towels = input[0].split(',')
  problems = input[2:]
  root = Trie()
  ans = 0
  for towel in towels:
    add(root, towel.strip())
  for towel in problems:
    ans += int(count(root, towel.strip()) != 0)
  return ans

def sln2(input):
  towels = input[0].split(',')
  problems = input[2:]
  root = Trie()
  ans = 0
  for towel in towels:
    add(root, towel.strip())
  for towel in problems:
    ans += count(root, towel.strip())
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))