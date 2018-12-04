
from util import get_data

class Map:
	matrix = []
	overlaps = 0

	def __init__(self, width, height):
		print("Created new map")
		self.matrix = [[0 for x in range(width)] for y in range(height)]
		self.overlaps = 0

	def add_section(self, startx, starty, height, width):
		# print('startx {}, starty {}, height {}, width {}'.format(startx, starty, height, width))
		for y in range(height):
			for x in range(width):
				if self.matrix[starty + y][startx + x] == 1:
					self.overlaps += 1
				self.matrix[starty + y][startx + x] += 1

	def print_overlaps(self):
		print('Total overlaps:', self.overlaps)

	def print_map_to_file(self):
		f = open("map.txt", "w+")
		for index in self.matrix:
			line = ''.join(str(e) for e in index)
			f.write(line)
			f.write('\n')

#	str1 = ''.join(str(e) for e in list1)

class Rectangle:
	startx = 0
	starty = 0
	height = 0
	width = 0

	def __init__(self, x, y, height, width):
		self.startx = int(x)
		self.starty = int(y)
		self.height = int(height)
		self.width = int(width)

	def print_info(self):
		print('start position: ({}, {})'.format(self.startx, self.starty))
		print('height: {}, width: {}'.format(self.height, self.width))

	def get_x(self):
		return self.startx

	def get_y(self):
		y = self.starty
		return y

	def get_width(self):
		width = self.width
		return width

	def get_height(self):
		height = self.height
		return height


def get_info(info):
	index = 0
	with open("../day3_input.txt", "r") as file:
		for line in file:
			line = line.rstrip('\n')
			line = line.rsplit(' ')
			coords = line[2]
			coords = coords.rstrip(':')
			coords = coords.rsplit(',')
			dimensions = line[3]
			dimensions = dimensions.rsplit('x')
			info[index] = Rectangle(coords[1], coords[0], dimensions[0], dimensions[1])
			index += 1
		file.close()

def check_overlaps():
	info = {}
	get_info(info)
	map = Map(1100, 1100)
	for index in info:
		# info[index].print_info()
		x = info[index].get_x()
		y = info[index].get_y()
		width = info[index].get_width()
		height = info[index].get_height()
		map.add_section(x, y, width, height)
	map.print_overlaps()
	map.print_map_to_file()

def run():
	check_overlaps()

run()
