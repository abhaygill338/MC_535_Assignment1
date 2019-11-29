import os
import sys
import test
import list

def streaming_data_items_daywise(list_items):
	return list_items
     
def storing_frequency_data(data_item,dict_freq):
	for i in range(0,len(data_item)):
		if(data_item[i] != ""):
			dict_freq[data_item[i]] = dict_freq.get(data_item[i],0)+1

	return dict_freq

def find_frequency_max_items_in_a_cycle(dict_freq, no_of_items):
	count = 0
	list_items_frequent = []
	for key,value in sorted(dict_freq.items(), key=lambda p:p[1], reverse=True):
		if(count == no_of_items):
			break
		print(key,value)
		list_items_frequent.append(key)
		count += 1

	return list_items_frequent

def missing_items_present(list_items_frequent,latest_data):
	flag = False
	for i in range(0,len(list_items_frequent)):
		flag = False
		for j in range(0,len(latest_data)):
			if(list_items_frequent[i] == latest_data[j]):
				flag = True
				break
		if(flag == False):
			print(list_items_frequent[i]," ")

if __name__ == '__main__':
	
	ch = 'Y'
	dict_freq = {}
	test.create_tables()
	list_items,date_list = list.getting_all_data()
	for i in range(0,len(date_list)):
		data_item = streaming_data_items_daywise(list_items[i])
		text = ""
		for j in range(0,len(data_item)):
			text += data_item[j]+','
		test.insert_item(date_list[i],text)
	#print('How many cycle days of data did we need')
	#cycle = int(input())
	cycle = 30
	all_data = test.data_based_on_cycle(cycle)
	for i in range(0,len(all_data)):
		all_data_list = all_data[i].split(",")
		print(all_data_list," ")
		storing_frequency_data(all_data_list,dict_freq)
	print(dict_freq)
	#print('What number of maximum long-lasting items needed ?')
	#no_of_items = int(input())
	no_of_items = 5
	print('Maximum number of long-lasting items needed in a particular cycle')
	list_items_frequent = find_frequency_max_items_in_a_cycle(dict_freq, no_of_items)
	print('Missing items that the user need to buy...')
	missing_items_present(list_items_frequent,all_data_list)