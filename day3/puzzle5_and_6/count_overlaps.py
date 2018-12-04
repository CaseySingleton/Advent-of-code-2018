
# Thanks to mserrano and her answer on /r/adventofcode
# This here is pretty much a direct copy. But took me about 12 hours until I had a
# pretty alright understanding of what's going on here

from collections import defaultdict
import re

filename = "../day3_input.txt"
cloth = defaultdict(list)
overlaps = {}
data = []

with open(filename, "r") as f:
	for line in f:
		data.append(line)

claims = map(lambda s: map(int, re.findall(r'-?\d+', s)), data)

for (claim_number, start_x, start_y, width, height) in claims:
	# print('claim #: {}, x: {}, y: {}, width: {}, height: {}'.format(claim_number, start_x, start_y, width, height))
	overlaps[claim_number] = set()
	for x in range(start_x, start_x + width):
		for y in range(start_y, start_y + height):
			if cloth[(x, y)]:
				for number in cloth[(x, y)]:
					overlaps[number].add(claim_number)
					overlaps[claim_number].add(number)
			cloth[(x, y)].append(claim_number)

print('Total number of overlaps:', len([j for j in cloth if len(cloth[j]) > 1]))
print('Claim(s) with no overlaps:', [k for k in overlaps if len(overlaps[k]) == 0][0])
