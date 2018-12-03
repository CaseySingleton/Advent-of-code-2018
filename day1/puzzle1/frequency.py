
with open("input.txt", "r") as file:
	frequency = sum(int(num) for num in file)
	print(frequency)
