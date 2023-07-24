import json
import os

class Table:

	def __init__(self, id, name, cost, start, end, a, b, hour, item, total_cost,is_active):
		self.id = id
		self.name = name
		self.cost = cost
		self.start = start
		self.end = end
		self.a = a
		self.b = b
		self.hour = hour
		self.item = item
		self.total_cost = total_cost
		self.is_active = is_active

class Table_list:
	def __init__(self, id, name):
		self.id = id
		self.name = name

def addtable():
	filename = "table_lst.txt"
	if not os.path.exists(filename):
		with open(filename, "w") as file:
				file.write("[]")
		length = 0
	else:
		with open(filename, "r") as file:
			data = file.read().strip()
			data_py = json.loads(data)
		length = len(data_py)
		
	table = []
	table_lst = []
	id = length + 1
	name = input("Table name: ")
	cost = 0
	start = 0
	end = 0
	a = 0
	b = 0
	hour = 0
	item = "test"
	total_cost = 0
	is_active = 0
	
	table.append(Table(id, name, cost, start, end, a, b, hour, item, total_cost, is_active))
	table_lst.append(Table_list(id, name))
	
	table_dict = [table[0].__dict__]
	table_json = json.dumps(table_dict)

	with open(f"{name}.txt", "w") as file:
		file.write(table_json)
		
	with open(filename, "r") as file:
		data = file.read().strip()
		data_py = json.loads(data)
		table_lst_dict = [i.__dict__ for i in table_lst]
		
	combine = data_py + table_lst_dict
	with open(filename, "w") as file:
		file.write(json.dumps(combine))
		
	return table_json


	








	

