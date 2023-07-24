import json
import os
import export

class Products:

	def __init__(self, id, name, price):
		self.id = id
		self.name = name
		self.price = price


def add_item(filename):
	
	if os.path.exists(filename):
		with open(filename, "r") as file:
			data = file.read().strip()
			data_py = json.loads(data)
		length = len(data_py)
	else:
		export.create_txt(filename)
		with open(filename, "w") as file:
			file.write("[]")
		length = 0

	print("last id: ", length)
	lst = []
	amount = int(input("How many item you want to add: "))
	for i in range(amount):
		name = input("Item name: ")
		price = int(input("Price: "))
		id = length + i + 1
		lst.append(Products(id, name.lower(), price))
	return lst

