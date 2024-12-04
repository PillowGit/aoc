from pathlib import Path
from .. import utils as u

def check_square(grid: list[list[str]], i: int, j: int) -> int:
  n,m = len(grid), len(grid[0])
  a = 0
  for di in range(-1, 2):
    for dj in range(-1, 2):
      if di == 0 and dj == 0:
        continue
      x,y = i,j
      for c in 'XMAS':
        if x not in range(m) or y not in range(n) or grid[x][y] != c:
          break
        x += di
        y += dj
      else:
        a += 1
  return a

def sln1(input):
  n,m = len(input), len(input[0])
  ans = 0
  for i in range(n):
    for j in range(m):
      ans += check_square(input, i, j)
  return ans

def check_x_mas(grid: list[list[str]], i: int, j: int) -> bool:
  n,m = len(grid), len(grid[0])
  if grid[i][j] != 'A': # not an 'a', can't be center of x shaped 'MAS'
    return False
  if i < 1 or i >= n-1 or j < 1 or j >= m-1: # edge of grid
    return False
  # top left to bottom right
  if not ((grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M')):
    return False
  # top right to bottom left
  if not ((grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M')):
    return False
  return True

# day 2 1 line
#print((lambda c,input:sum(int(c(input, i, j)) for i in range(len(input)) for j in range(len(input[0]))))(lambda grid, i, j: grid[i][j]=='A' and (not (i not in range(1, len(grid)-1) or j not in range(1,len(grid[0])-1))) and (not ((not ((grid[i-1][j-1] == 'M' and grid[i+1][j+1] == 'S') or (grid[i-1][j-1] == 'S' and grid[i+1][j+1] == 'M'))) or (not ((grid[i-1][j+1] == 'M' and grid[i+1][j-1] == 'S') or (grid[i-1][j+1] == 'S' and grid[i+1][j-1] == 'M'))))),[[c for c in x] for x in open('4.txt').read().strip().split('\n')])) 
 
def sln2(input):
  n,m = len(input), len(input[0])
  ans = 0
  for i in range(n):
    for j in range(m):
      ans += int(check_x_mas(input, i, j))
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.grid(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))