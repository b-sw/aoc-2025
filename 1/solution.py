moves = []

for line in open('input.txt'):
	dir, stepsCount = line[0], int(line[1:])
	moves.append((dir, stepsCount))

def part1():
	current = 50
	zeroesSeen = 0

	for dir, stepsCount in moves:
		if dir == 'L':
			current = (current - stepsCount) % 100
		else:
			current = (current + stepsCount) % 100

		if current == 0:
			zeroesSeen += 1

	return zeroesSeen

print(part1())

def part2():
	current = 50
	zeroesSeen = 0

	for dir, stepsCount in moves:
		zeroesSeen += (stepsCount // 100)
		stepsCount %= 100

		start = current
		current = (current + stepsCount * (1 if dir == 'R' else -1))
		
		if start != 0 and (current <= 0 or current >= 100):
			zeroesSeen += 1
		
		current %= 100

	return zeroesSeen

print(part2())