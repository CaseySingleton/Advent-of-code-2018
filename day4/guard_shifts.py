from collections import defaultdict
lines = open("day4_input.txt").read().split('\n')
lines.sort()

# Make this get the guard that sleeps the most and can figure out the most
# frequently slept minute given a list

def get_minute(line):
	words = line.split()
	time = words[1][:-1]
	return (int(time.split(':')[1]))

def get_hour(line):
	words = line.split()
	time = words[1][1:]
	return (int(time.split(':')[0]))

def get_guard_number(line):
	words = line.split()
	guard_number = words[3][1:]
	return (int(guard_number))

def is_asleep(line):
	if 'wake' in line:
		return (True)
	elif 'asleep' in line:
		return (False)

def greatest_in_dict(d):
	best = None
	for guard,minute in d.items():
		if best is None or minute > d[best]:
			best = guard
	return (best)

def get_record(record):
	guard = None
	time = None
	start_sleep = None
	most_slept = defaultdict(int)

	for line in lines:
		time = get_minute(line)
		if 'Guard' in line:
			guard = get_guard_number(line)
			start_sleep = None
		elif 'asleep' in line:
			start_sleep = time
		elif 'wake' in line:
			for num in range(start_sleep, time):
				record[(guard, num)] += 1
				most_slept[guard] += 1
				# print("guard: {} ".format(guard))
	y = None
	for x in most_slept:
		if y is None or y < most_slept[x]:
			y = most_slept[x]
			name = x
	print('Guard:', name, 'Total Hours:', y)
	for i in range(59):
		print('Minute:', i, 'Overlaps:', record[(name, i)])

record = defaultdict(int)
get_record(record)
# for g, m in record:
# 	print('For:', g, 'Minute:', m, 'Total time:', record[(g, m)])

guard, minute = greatest_in_dict(record)
print('Best guard:', guard, 'Best minute:', minute),
print('Answer:', guard * minute)
