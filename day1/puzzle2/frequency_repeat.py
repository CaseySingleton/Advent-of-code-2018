
nums = {"0" : 1}
done = False
frequency = 0

while done == False:
	with open("input.txt", "r") as file:
		for line in file:
			frequency += int(line)
			if nums.get(frequency) == 1:
				done = True
				break
			else:
				nums[frequency] = 1
	file.close()
print("repeat: ", frequency)
