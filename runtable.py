import json
import time
import os

current_time = time.time()
time_struct = time.localtime(current_time)
hour = time_struct.tm_hour
min = time_struct.tm_min
second = time_struct.tm_sec
year = time_struct.tm_year
month = time_struct.tm_mon
day = time_struct.tm_mday


def get_current_time():
	current_time = str(year) + str(month) + str(day) + "-" + str(hour) + ":" + str(min) + ":" + str(second)
	return current_time


def open_time():
	start = time.time()
	return start


def close_time():
	end = time.time()
	return end


def load_table_data(filename):
	with open(filename, "r") as file:
		data = file.read().strip()
		table_py = json.loads(data)
	return table_py


def export_table_data(filename, data):
	with open(filename, "w") as file:
		data_json = json.dumps(data)
		file.write(data_json)


def open_table(filename, id):
	table_py = load_table_data(filename)
	for i in range(len(table_py)):
		if table_py[i]["id"] == id:
			print(f"Succeed open table {table_py[i]['id']}")
			table_py[i]["is_active"] = 1
			table_py[i]["start"] = get_current_time()
			table_py[i]["end"] = ""
			table_py[i]["hour"] = 0
			table_py[i]["a"] = round(time.time(),0)
			print(table_py)
	return table_py


def close_table(filename, id):
	table_py = load_table_data(filename)
	
	for i in range(len(table_py)):
		if table_py[i]["id"] == id:
			print(f"succeed close table {table_py[i]['id']}")
			table_py[i]["is_active"] = 0
			table_py[i]["end"] = get_current_time()
			table_py[i]["b"] = round(time.time(),0)
			table_py[i]["hour"] = round((time.time() - table_py[i]["a"]) / 3600, 2)

			print(table_py)
	return table_py
