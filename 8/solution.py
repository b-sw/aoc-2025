import math

points = [list(map(int, line.split(','))) for line in open('input.txt').read().splitlines()]

def part1():
  dists = []

  for pi in range(len(points) - 1):
    for oi in range(pi + 1, len(points)):
      dist = math.sqrt((points[pi][0] - points[oi][0])**2 + (points[pi][1] - points[oi][1])**2 + (points[pi][2] - points[oi][2])**2)
      dists.append((pi, oi, dist))

  dists.sort(key=lambda d: d[2])
  
  shortest = dists[:1000]
  graph = dict()
  for connection in shortest:
    n1, n2, _ = connection
    if n1 not in graph:
      graph[n1] = []
    if n2 not in graph:
      graph[n2] = []
    graph[n1].append(n2)
    graph[n2].append(n1)

  visited = set()
  circuitsSizes = []
  for node in graph.keys():
    if node in visited:
      continue

    circuitsSizes.append(dfs(node, graph, set(), visited))

  result = 1
  circuitsSizes.sort(reverse=True)
  for size in circuitsSizes[:3]:
    result *= size
  return result

def dfs(node, graph, currentlyVisited, overallyVisited):
  result = 1
  currentlyVisited.add(node)
  overallyVisited.add(node)

  for neighbor in graph.get(node, []):
    if neighbor not in currentlyVisited:
      result += dfs(neighbor, graph, currentlyVisited, overallyVisited)

  return result

def part2():
  dists = []
  for pi in range(len(points) - 1):
    for oi in range(pi + 1, len(points)):
      dist = math.sqrt((points[pi][0] - points[oi][0])**2 + (points[pi][1] - points[oi][1])**2 + (points[pi][2] - points[oi][2])**2)
      dists.append((pi, oi, dist))
  dists.sort(key=lambda d: d[2])

  pointsCount = len(points)
  seen = set()

  graph = dict()
  for connection in dists:
    n1, n2, _ = connection
    if n1 not in graph:
      graph[n1] = []
    if n2 not in graph:
      graph[n2] = []
    graph[n1].append(n2)
    graph[n2].append(n1)

    if dfs(0, graph, set(), set()) == pointsCount:
      return points[n1][0] * points[n2][0]

  raise Exception('bad solution')

print(part1())
print(part2())
