from pathlib import Path
from .. import utils as u
from rich import print
from shapely.geometry import Polygon

def square(a, b):
  return (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)

def sln1(pts):
  ans = -1
  for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
      ans = max(ans, square(pts[i], pts[j]))
  return ans

def sln2(pts):
  ans = -1
  shape = Polygon(pts)
  for i in range(len(pts)):
    for j in range(i + 1, len(pts)):
      a, b = pts[i], pts[j]
      rect = Polygon([(a[0], a[1]), (a[0], b[1]), (b[0], b[1]), (b[0], a[1])])
      if shape.contains(rect):
        ans = max(ans, square(pts[i], pts[j]))
  return ans

if __name__ == '__main__':
  this_file = Path(__file__).resolve()
  day = this_file.stem
  input_file = this_file.parent / f'{day}.txt'
  
  # Use any parsing method here
  parsed_input = [tuple(map(int, line.split(','))) for line in open(input_file).read().strip().split('\n')]

  print('Part 1:', sln1(parsed_input))
  print('Part 2:', sln2(parsed_input))