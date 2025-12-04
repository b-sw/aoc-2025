grid = [list(line) for line in open('input.txt').read().splitlines()]

def removeRolls():
  result = 0
  toRemove = []
  rows, cols = len(grid), len(grid[0])
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] != '@':
        continue

      adjacentCount = 0
      for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if 0 <= r + dr < rows and 0 <= c + dc < cols and grid[r + dr][c + dc] == '@':
          adjacentCount += 1

      if adjacentCount < 4:
        result += 1
        toRemove.append((r, c))

  return result, toRemove

def part1():
  return removeRolls()[0]

def part2():
  totalRollsRemoved = 0

  while True:
    result, toRemove = removeRolls()
    if result == 0:
      break
    for r, c in toRemove:
      grid[r][c] = '.'

    totalRollsRemoved += result

  return totalRollsRemoved

print(part1())
print(part2())