
def get_info( info ):
	index = 0
	with open("../day2_input.txt", "r") as file:
		for line in file:
			info[index] = line.rstrip()
			index += 1
		file.close()

def get_diff():
	info = {}

	get_info(info)
	for x in info:
		y = x + 1
		for y in info:
			diff = 0
			for index in range(len(info[x])):
				if info[x][index] != info[y][index]:
					diff += 1
			if diff == 1:
				print('s1', info[x])
				print('s2', info[y])
				print('index:', index, 'chars:', info[x][index], info[y][index])
				return

get_diff()
