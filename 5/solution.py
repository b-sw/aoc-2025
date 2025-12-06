ranges, ids = open('input.txt').read().split('\n\n')
ranges = [[int(start), int(end)] for start, end in [range.split('-') for range in ranges.splitlines()]]
ids = [int(id) for id in ids.splitlines()]

def part1():
  # sort & merge ranges
  sortedRanges =  sorted(ranges, key=lambda range: range[0])
  mergedRanges = getMergedRanges(sortedRanges)
  
  # solve with bfs
  result = 0
  for id in ids:
    if binarySearch(id, mergedRanges):
      result += 1
  return result

def getMergedRanges(sortedRanges):
  mergedRanges = [sortedRanges[0]]

  mi = 0
  for i in range(1, len(sortedRanges)):
    if sortedRanges[i][0] > mergedRanges[mi][1]:
      mergedRanges.append(sortedRanges[i])
      mi += 1
    else:
      mergedRanges[mi][1] = max(mergedRanges[mi][1], sortedRanges[i][1])
  
  return mergedRanges

def binarySearch(target, mergedRanges): 
  left, right = 0, len(mergedRanges)

  while left < right:
    mid = (left + right) // 2

    if target > mergedRanges[mid][1]:
      left = mid + 1
    else:
      right = mid

  return False if left == len(mergedRanges) else mergedRanges[left][0] <= target <= mergedRanges[left][1]

def part2():
  # sort & merge ranges
  sortedRanges =  sorted(ranges, key=lambda range: range[0])
  mergedRanges = getMergedRanges(sortedRanges)

  result = 0

  for r in mergedRanges:
    result += (r[1] - r[0] + 1)

  return result

print(part1())
print(part2())