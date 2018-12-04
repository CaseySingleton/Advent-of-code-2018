
doubles = 0
triples = 0
letters = "abcdefghijklmnopqrstuvwxyz"
get_double = True
get_triple = True
count = 0

with open("../day2_input.txt", "r") as file:
	for line in file:
		get_double = True
		get_triple = True
		for letter in letters:
			if get_double == False and get_triple == False:
				break
			count = line.count(letter)
			if count == 2 and get_double == True:
				doubles += 1
				get_double = False
			elif count == 3 and get_triple == True:
				triples += 1
				get_triple = False
	print('doubles:', doubles, 'triples:', triples)
	print('checksum:', doubles * triples)
	file.close()