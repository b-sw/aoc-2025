import re
lines = open('input.txt').read().splitlines()

numsLines = [list(map(int, line.split())) for line in lines[:-1]]
ops = lines[-1].split()

def part1():
  problems = [[] for _ in range(len(numsLines[0]))]

  for nums in numsLines:
    for i in range(len(nums)):
      problems[i].append(nums[i])

  result = 0
  for pi in range(len(problems)):
    op = ops[pi]
    res = 0 if op == '+' else 1
    for num in problems[pi]:
      res = res + num if op == '+' else res * num
    result += res

  return result

def part2():
  pi = 0
  totalSum = 0
  result = 0 if ops[pi] == '+' else 1

  for c in range(len(lines[0])):
    if all(line[c] == ' ' for line in lines[:-1]):
      pi += 1
      totalSum += result
      result = 0 if ops[pi] == '+' else 1
      continue

    cephalopodNum = []
    for line in lines[:-1]:
      if line[c] != ' ':
        cephalopodNum.append(line[c])

    cephalopodNum = int(''.join(cephalopodNum))

    result = result + cephalopodNum if ops[pi] == '+' else result * cephalopodNum

  return totalSum + result

print(part1())
print(part2())