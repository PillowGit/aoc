from pathlib import Path
from .. import utils as u

from rich import print
from collections import defaultdict

def is_valid(rules, pages):
  remaining_pages = set(pages)
  seen = set()
  for page in pages:
    remaining_pages.remove(page)
    if rules[page] & remaining_pages:
      return False
    seen.add(page)
  return True

def fix_pages(rules, pages):
  for i in range(len(pages)):
    remaining_pages = set(pages[i:])
    for j, page in enumerate(pages):
        if j < i: continue
        if not rules[page] & remaining_pages:
            pages[i], pages[j] = pages[j], pages[i]
            break
  return pages

def sln1(input):
  rule_input, page_input = input.split('\n\n')
  rules = defaultdict(set)
  for line in rule_input.split('\n'):
    a, b = line.split('|')
    rules[b].add(a)
  pages = [x.split(',') for x in page_input.split('\n')]

  ans = 0
  for page_seq in pages:
    if is_valid(rules, page_seq):
      ans += int(page_seq[len(page_seq) // 2])
  return ans

def sln2(input):
  rule_input, page_input = input.split('\n\n')
  rules = defaultdict(set)
  for line in rule_input.split('\n'):
    a, b = line.split('|')
    rules[b].add(a)
  pages = [x.split(',') for x in page_input.split('\n')]

  ans = 0
  for page_seq in pages:
    if not is_valid(rules, page_seq):
      ans += int(fix_pages(rules, page_seq)[len(page_seq) // 2])
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  parsed_input = u.parsing.text(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))