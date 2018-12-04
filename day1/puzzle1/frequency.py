
with open("../day1_input.txt", "r") as file:
	frequency = sum(int(num) for num in file)
	print('frequency:', frequency)
	file.close()
