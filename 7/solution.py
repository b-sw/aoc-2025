grid = open('input.txt').read().splitlines()
startRow, startCol = 0, grid[0].index('S')

def part1():
  maxR, maxC = len(grid), len(grid[0])
  queue = [(startRow, startCol)]
  visited = set()
  splitsCount = 0

  while queue:
    r, c = queue.pop()

    visited.add((r, c))

    if grid[r][c] != '^':
      if r + 1 < maxR and (r + 1, c) not in visited:
        queue.append((r + 1, c))
    elif grid[r][c] == '^':
      splitsCount += 1
      if c - 1 >= 0 and (r, c - 1) not in visited:
        queue.append((r, c - 1))
      if c + 1 < maxC and (r, c + 1) not in visited:
        queue.append((r, c + 1))
    
  return splitsCount

def part2():
  maxR, maxC = len(grid), len(grid[0])
  dp = [[1] * maxC for _ in range(maxR)]

  for r in range(maxR - 2, -1, -1):
    for c in range(maxC):
      if grid[r][c] != '^':
        dp[r][c] = dp[r + 1][c]
      else:
        dp[r][c] = dp[r + 1][c - 1] + dp[r + 1][c + 1]

  return dp[startRow][startCol]

print(part1())
print(part2())