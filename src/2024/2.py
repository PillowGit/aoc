from pathlib import Path
from .. import utils as u

# 1 lines (assuming input is called '2.txt' and exists where u run this from)
# part 1
print((lambda check, input:sum(int(check([int(x) for x in l.split()])) for l in input))(lambda l: all(abs(l[i] - l[i-1]) in range(1, 4) for i in range(1, len(l))) and (sorted(l) == l or sorted(l, reverse=True) == l),open('2.txt').read().splitlines()))
# part 2
print((lambda check, input:sum((lambda l:int(any(check(t) for t in ([l] + [l[:i]+l[i+1:] for i in range(len(l))]))))([int(x) for x in l.split()]) for l in input))(lambda l: all(abs(l[i] - l[i-1]) in range(1, 4) for i in range(1, len(l))) and (sorted(l) == l or sorted(l, reverse=True) == l),open('2.txt').read().splitlines()))

def check(l):
  return all(abs(l[i] - l[i-1]) in range(1, 4) for i in range(1, len(l))) and (sorted(l) == l or sorted(l, reverse=True) == l)

def sln1(input):
  return sum(int(check([int(x) for x in l.split()])) for l in input)

def sln2(input):
  return sum((lambda l:int(any(check(t) for t in ([l] + [l[:i]+l[i+1:] for i in range(len(l))]))))([int(x) for x in l.split()]) for l in input)

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))