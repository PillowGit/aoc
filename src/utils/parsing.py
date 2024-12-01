from pathlib import Path

# Basic reading

def read(file: Path) -> str:
  with file.open() as f:
    return f.read().strip()

# Lines

def lines(file: Path) -> list[str]:
  with file.open() as f:
    return f.read().strip().split('\n')

def lines_as_ints(file: Path) -> list[int]:
  with file.open() as f:
    return [int(x) for x in f.read().strip().split('\n')]

# Grids

def grid(file: Path) -> list[list[str]]:
  with file.open() as f:
    return [list(x) for x in f.read().strip().split('\n')]

def grid_as_ints(file: Path) -> list[list[int]]:
  with file.open() as f:
    return [[int(y) for y in x] for x in f.read().strip().split('\n')]