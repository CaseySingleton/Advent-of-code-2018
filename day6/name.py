def get_info_from_file(coords:)
	with open("day6_input.txt", "r") as f:
		for line in f:
			print(line.rstrip('\n'))
			coord = []