from pathlib import Path
from .. import utils as u
from rich import print

# One liner
print([h:=[r:=(lambda g: [c:=[(r,c) for r in range(len(g)) for c in range(len(g[0])) if g[r][c]=='@'],t:=[([(r+dr, c+dc) for dr in [-1, 0, 1] for dc in [-1, 0, 1] if ((dr != 0 or dc != 0) and (r+dr) in range(len(g)) and (c+dc) in range(len(g[0])) and g[r+dr][c+dc] == '@')] + [(r,c)]) for r,c in c],gg:=list(filter(lambda x: len(x) < 5, t)),s:=set(x[-1] for x in gg),(len(gg),[[g[r][c] if (r,c) not in s else 'x' for c in range(len(g[0]))] for r in range(len(g))])][-1]),r([list(i) for i in open('/home/pillow/git-repos/aoc/src/2025/4.txt').read().strip().split('\n')])[0],sum([e:=[list(i) for i in open('/home/pillow/git-repos/aoc/src/2025/4.txt').read().strip().split('\n')],[[o:=r(e), e:=o[1], o[0]][-1] for _ in range(100)]][-1])], f'Part 1: {h[-2]}\nPart 2: {h[-1]}'][-1])

def iterate(input, part2=False):
  removed = 0
  n, m = len(input), len(input[0])
  dirs = [(-1,-1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  for r in range(n):
    for c in range(m):
      if input[r][c] == '@':
        adj = 0
        for dr, dc in dirs:
          nr, nc = r + dr, c + dc
          if nr in range(n) and nc in range(m) and input[nr][nc] == '@':
            adj += 1
        if adj < 4:
          removed += 1
          if part2: input[r][c] = '.'
  return removed

def sln1(input):
  return iterate(input)

def sln2(input):
  ans = 0
  while True:
    removed = iterate(input, True)
    if removed == 0:
      break
    ans += removed
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [list(line) for line in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))