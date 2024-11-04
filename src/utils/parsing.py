from pathlib import Path

def read(file: Path) -> str:
  with file.open() as f:
    return f.read().strip()

def lines(file: Path) -> list[str]:
  with file.open() as f:
    return f.read().strip().split('\n')