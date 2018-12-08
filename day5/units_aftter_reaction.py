def check_for_error(data):
	index = 1
	while (index in range(len(data))):
		c1 = ord(data[index - 1])
		c2 = ord(data[index])
		if (abs(c1 - c2) == 32):
			print('Error at the indices: {} and {}\nContent: {} {}'.format(index - 1, index, data[index - 1], data[index]))
		index += 1

def reaction(s, index):
	while index < len(s) and index > 0:
		c1 = ord(s[index])
		c2 = ord(s[index - 1])
		if abs(c1 - c2) is 32:
			del(s[index])
			del(s[index - 1])
			index -= 1
			continue
		break
	return (index + 1)

def solution(data):
	index = 0
	before = len(data)
	while index in range(len(data)):
		index = reaction(data, index)
	after = len(data)
	check_for_error(data)
	print('Before reaction: {} After reaction: {}'.format(before, after))
	f.close()

with open("day5_input.txt", "r") as f:
	master = f.read()
	alphabet = 'abcdefghijklmnopqrstuvwxyz'
	for letter in alphabet:
		print(letter, end = ': ')
		master_copy = master.replace(letter, '')
		master_copy = master_copy.replace(letter.upper(), '')
		# print(master_copy)
		data = list(master_copy)
		solution(data)
	# solution(data)
