from pathlib import Path

def lines(file: Path) -> list[str]:
  with file.open() as f:
    return f.read().strip().split('\n')