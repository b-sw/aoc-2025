lines = [line.split(' ') for line in open('input.txt').read().splitlines()]
targets = [line[0][1:-1] for line in lines]
buttonsRaw = [line[1: -1] for line in lines]
joltages = [list(map(int, line[-1][1:-1].split(','))) for line in lines]
buttonsSets = []

for br in buttonsRaw:
  tmpButtons = []
  for button in br:
    tmpButtons.append(list(map(int, button[1:-1].split(','))))
  buttonsSets.append(tmpButtons)

def part1():
  pushesCount = 0
  for i in range(len(targets)):
    target, buttons = targets[i], buttonsSets[i]
    pushesCount += findMinModulo(target, [False] * len(target), 0, buttons, 0)

  return pushesCount

def findMinModulo(target, current, bi, buttons, pushedCount):
  if bi == len(buttons):
    if matches(target, current):
      return pushedCount
    else:
      return float('inf')
  
  button = buttons[bi]
  
  for b in button:
    current[b] = not current[b]
  res1 = findMinModulo(target, current, bi + 1, buttons, pushedCount + 1)
  for b in button:
    current[b] = not current[b]

  res2 = findMinModulo(target, current, bi + 1, buttons, pushedCount)

  return min(res1, res2)

def matches(target, current):
  for i in range(len(target)):
    if target[i] == '#' and not current[i]:
      return False
    if target[i] == '.' and current[i]:
      return False
  return True

print(part1())