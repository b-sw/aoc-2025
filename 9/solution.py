coords = [tuple(map(int, line.split(','))) for line in open('input.txt').read().splitlines()]

def part1():
  maxS = 0
  for i in range(len(coords) - 1):
    for j in range(i + 1, len(coords)):
      p1, p2 = coords[i], coords[j]
      maxS = max(maxS, abs(p1[0] - p2[0] + 1) * abs(p1[1] - p2[1] + 1))

  return maxS

def part2():
  rows, cols = max([coord[1] for coord in coords]), max([coord[0] for coord in coords])
  grid = ['.' * (cols + 1) for _ in range(rows + 1)]

  oldC, oldR = coords[0]
  grid[oldR] = grid[oldR][:oldC] + '#' + grid[oldR][oldC + 1:]

  for point in coords[1:]:
    c, r = point
    grid[r] = grid[r][:c] + '#' + grid[r][c + 1:]

    if oldR == r:
      if oldC < c:
        grid[r] = grid[r][:oldC] + '#' * (c - oldC + 1) + grid[r][c + 1:]
      else:
        grid[r] = grid[r][:c] + '#' * (oldC - c + 1) + grid[r][oldC + 1:]
    elif oldC == c:
      if oldR < r:
        for tmpR in range(oldR + 1, r):
          grid[tmpR] = grid[tmpR][c:] + '#' + grid[tmpR][c + 1:]
      else:
        for tmpR in range(r + 1, oldR):
          grid[tmpR] = grid[tmpR][c:] + '#' + grid[tmpR][c + 1:]
    
    oldR, oldC = r, c

    for row in grid:
      print(row)
    print()


print(part1())
print(part2())