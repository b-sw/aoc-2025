banks = [list(map(int, line)) for line in open('input.txt').read().splitlines()]

def solve(subbankSize: int):
  result = 0

  for bank in banks:
    left, right = 0, len(bank) - subbankSize + 1
    subbank = []
    while right <= len(bank):
      nextMax = max(bank[left:right])
      subbank.append(nextMax)
      left = bank[left:].index(nextMax) + 1 + left
      right += 1

    result += int(''.join(map(str, subbank)))

  return result

print(solve(2))
print(solve(12))