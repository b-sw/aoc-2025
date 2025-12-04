ranges = [range.split('-') for range in open('input.txt').read().split(',')]

def solve(isInvalidFn: callable):
	invalidSum = 0

	for idsRange in ranges:
		start, end = int(idsRange[0]), int(idsRange[1])

		for i in range(start, end + 1):
			if isInvalidFn(i):
				invalidSum += i

	return invalidSum

def isInvalid(num: int) -> bool:
	sNum = str(num)

	return sNum[:len(sNum) // 2] == sNum[len(sNum) // 2:]

def isInvalidPart2(num: int) -> bool:
	sNum = str(num)

	for i in range(1, len(sNum) // 2 + 1):
		if len(sNum) % i != 0:
			continue

		repeatedSubstring = sNum[:i]

		for j in range(i, len(sNum) - i + 1, i):
			if sNum[j:j+i] != repeatedSubstring:
				break
		else:
			return True

	return False

print(solve(isInvalid))
print(solve(isInvalidPart2))