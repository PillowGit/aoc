# Returns the overlap given two ranges

def find_overlap(start1: int, end1: int, start2: int, end2: int) -> tuple[int, int] | None:
  maxStart = max(start1, start2)
  minEnd = min(end1, end2)
  if maxStart <= minEnd:
    return (maxStart, minEnd)
  else:
    return None