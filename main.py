import additem
import addtable
import export
import runtable

import json

class Order_lst:
	def __init__(self, name, price):
		self.name = price
		self.price = price
	

def load_txt(filename):
	with open(filename, "r") as file:
		data_json = file.read().strip()
		data_dict = json.loads(data_json)
	return data_dict


def export_txt(filename, data):
	data_json = json.dumps(data)
	with open(filename, "w") as file:
		file.write(data_json)
		print(f"{filename} saved.")

def order_item_lst(item_txt):
	item_data = load_txt(item_txt)
	order = []
	amount = int(input("How many item buyer ordered?: "))
	for i in range(amount):
		id = int(input("Select item: "))
		item = item_data[id-1]
		order.append(item)
	
	for i in range(len(order)):
		print(order[i])
		
	return order


def order_item_storage_txt(table_id, order):
	filename = None
	table_lst = load_txt("table_lst.txt")
	for i in range(len(table_lst)):
		if table_id == table_lst[i]["id"]:
			filename = f"{table_lst[i]['name']}.txt"
			
	update_table = load_txt(filename)
	update_table[0]["item"] = json.dumps(order)
	print(update_table)
	

	print("Function no error.")
	
	


def main():

	while True:
		print("----------------")
		script = input("\nrun script: ")
		
		if script == "pick":
			#item_txt = "items_data_json.txt
			#add_item_to_table(item_txt)
			
			table_id = int(input("Select table to add item: "))
			
			item_txt = "items_data_json.txt"
			order = order_item_lst(item_txt)
			print(type(order))
			order_item_storage_txt(table_id, order)
			
		
			break
		

		elif script == "open":
			id = int(input("Open table: "))
			filename = f"vip {id}.txt"
			data = runtable.open_table(filename, id)
			export.export_txt(filename, data)
		
			break

		elif script == "close":
			id = int(input("Close table: "))
			filename = f"vip {id}.txt"
			data = runtable.close_table(filename, id)
			export.export_txt(filename, data)

			break
			
		elif script == "add table":
			table = addtable.addtable()
			print(table)

			break
			
			

		elif script == "add item":
			filename = "items_data_json.txt"
			update = additem.add_item(filename)
			print("Recent added: ")
			for i in range(len(update)):
				print(f"name: {update[i].name}")
				print(f"price: {update[i].price}")

			name_txt = "items_data_json.txt"
			export.export_item_txt(name_txt, update)

			name_xlsx = "items_data_xl.xlsx"
			#export.export_item_xlsx(name_xlsx, name_txt)
			
			break


		else:
			print("Invalid input.")


if __name__ == "__main__":
	main()

# export item-list.xlsx immediately once adding item to list ok
# convert json data to excel format ok
# excel report export ok
# create table ok

# add item order to table
# create bill accountant

# import data from excel
# automatic backup data
# excel task automation

# action history with time
# user mangement
# trial ver. and premium ver.

# report result with capture of reels
# improve set mouse position function for user using easily
# show button description when mouse hover

