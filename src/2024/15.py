from pathlib import Path
from .. import utils as u
from rich import print

def parse_input(input):
  map_lines, moves = [], []
  for line in input:
    if line.startswith('#'):
      map_lines.append(line)
    else:
      moves.append(line)
  grid = [list(line) for line in map_lines]
  robot = None
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '@':
        robot = (r, c)
        grid[r][c] = '.'
  return grid, robot, ''.join(moves)

DIRS = {
  '^': (-1, 0),
  '>': (0, 1),
  'v': (1, 0),
  '<': (0, -1)
}

def showgrid(grid, robot):
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if (r, c) == (round(robot[0]), round(robot[1])):
        print('@', end='')
      else:
        print(col, end='')
    print()

# 1483867
def sln1(input, debug = False):
  grid, robot, moves = parse_input(input)
  for move in moves:
    dr, dc = DIRS[move]
    nr, nc = robot[0] + dr, robot[1] + dc
    if nr not in range(len(grid)) or nc not in range(len(grid[0])):
      continue
    if grid[nr][nc] == '#':
      continue
    if grid[nr][nc] == 'O':
      sr, sc = nr, nc
      boxes_to_push = 0
      while ((sr in range(len(grid)) and sc in range(len(grid[0])))
             and grid[sr][sc] != '#' and grid[sr][sc] == 'O'):
        boxes_to_push += 1
        sr += dr
        sc += dc
      if debug: print(f"Starting swap at {sr}, {sc}. Will push {boxes_to_push} boxes")
      if sr not in range(len(grid)) or sc not in range(len(grid[0])) or grid[sr][sc] == '#':
        continue
      for _ in range(boxes_to_push):
        if debug: print(f"Swapping {sr}, {sc} with {sr-dr}, {sc-dc} ({grid[sr-dr][sc-dc]} -> {grid[sr][sc]})")
        grid[sr][sc], grid[sr-dr][sc-dc] = grid[sr-dr][sc-dc], grid[sr][sc]
        sr -= dr
        sc -= dc
      robot = (nr, nc)
    else:
      robot = (nr, nc)
    if debug: showgrid(grid, robot)
  ans = 0
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == 'O':
        ans += 100 * r + c
  return ans

def sln2(input, debug = False):
  grid, robot, moves = parse_input(input)
  newgrid = [[]]
  for row in grid:
    for c in row:
      if c == 'O':
        newgrid[len(newgrid)-1].append('[')
        newgrid[len(newgrid)-1].append(']')
      else:
        newgrid[len(newgrid)-1].append(c)
        newgrid[len(newgrid)-1].append(c)
    newgrid.append([])
  grid = newgrid[:-1]
  robot = (robot[0], 2 * robot[1])
  if debug: showgrid(grid, robot)
  def canmoveupordown(r, c, move):
    leftr, leftc = r, c
    rightr, rightc = r, c
    if grid[r][c] == '[':
      rightc += 1
    else:
      leftc -= 1
    leftup, rightup = None, None
    if move == '^':
      leftup = grid[leftr-1][leftc]
      rightup = grid[rightr-1][rightc]
    elif move == 'v':
      leftup = grid[leftr+1][leftc]
      rightup = grid[rightr+1][rightc]
    if leftup == '.' and rightup == '.':
      return True
    if leftup == '#' or rightup == '#':
      return False
    canmoveleft = leftup == '.' or canmoveupordown(leftr-1 if move == '^' else leftr+1, leftc, move)
    canmoveright = rightup == '.' or canmoveupordown(rightr-1 if move == '^' else rightr+1, rightc, move)
    return canmoveleft and canmoveright
  def movebox(r, c, move, verified = False):
    leftr, leftc = r, c
    rightr, rightc = r, c
    if grid[r][c] == '[':
      rightc += 1
    else:
      leftc -= 1
    if move == '>':
      next_space = grid[rightr][rightc+1]
      if next_space == '.':
        grid[leftr][leftc] = '.'
        grid[rightr][rightc] = '['
        grid[rightr][rightc+1] = ']'
        return True
      elif next_space == '#':
        return False
      elif next_space == '[':
        move_next = movebox(rightr, rightc+1, move)
        if not move_next:
          return False
        grid[leftr][leftc] = '.'
        grid[rightr][rightc] = '['
        grid[rightr][rightc+1] = ']'
        return True
    elif move == '<':
      next_space = grid[leftr][leftc-1]
      if next_space == '.':
        grid[rightr][rightc] = '.'
        grid[leftr][leftc] = ']'
        grid[leftr][leftc-1] = '['
        return True
      elif next_space == '#':
        return False
      elif next_space in '[]':
        move_next = movebox(leftr, leftc-1, move)
        if not move_next:
          return False
        grid[rightr][rightc] = '.'
        grid[leftr][leftc] = ']'
        grid[leftr][leftc-1] = '['
        return True
    elif move == '^':
      canmove = verified or canmoveupordown(leftr, leftc, move)
      if not canmove:
        return False
      leftup = grid[leftr-1][leftc]
      rightup = grid[rightr-1][rightc]
      if leftup == '[' and rightup == ']':
        moved = movebox(leftr-1, leftc, move, verified)
        if not moved:
          return False
        grid[leftr][leftc] = '.'
        grid[rightr][rightc] = '.'
        grid[leftr-1][leftc] = '['
        grid[rightr-1][rightc] = ']'
        return True
      if leftup == ']':
        movebox(leftr-1, leftc, move, verified)
      if rightup == ']':
        movebox(rightr-1, rightc, move, verified)
      grid[leftr][leftc] = '.'
      grid[rightr][rightc] = '.'
      grid[leftr-1][leftc] = '['
      grid[rightr-1][rightc] = ']'
      return True
    elif move == 'v':
      canmove = verified or canmoveupordown(leftr, leftc, move)
      if not canmove:
        return False
      leftup = grid[leftr+1][leftc]
      rightup = grid[rightr+1][rightc]
      if leftup == '[' and rightup == ']':
        moved = movebox(leftr+1, leftc, move, verified)
        if not moved:
          return False
        grid[leftr][leftc] = '.'
        grid[rightr][rightc] = '.'
        grid[leftr+1][leftc] = '['
        grid[rightr+1][rightc] = ']'
        return True
      if leftup == ']':
        movebox(leftr+1, leftc, move, verified)
      if rightup == ']':
        movebox(rightr+1, rightc, move, verified)
      grid[leftr][leftc] = '.'
      grid[rightr][rightc] = '.'
      grid[leftr+1][leftc] = '['
      grid[rightr+1][rightc] = ']'
      return True

  for move in moves:
    dr, dc = DIRS[move]
    nr, nc = robot[0] + dr, robot[1] + dc
    if nr not in range(len(grid)) or nc not in range(len(grid[0])):
      continue
    if grid[nr][nc] == '#':
      continue
    if grid[nr][nc] in '[]':
      moved = movebox(nr, nc, move)
      if moved:
        robot = (nr, nc)
    else:
      robot = (nr, nc)
    if debug: print(move)
    if debug: showgrid(grid, robot)
  ans = 0
  for r, row in enumerate(grid):
    for c, col in enumerate(row):
      if col == '[':
        ans += 100 * r + c
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = u.parsing.lines(input_file)

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))