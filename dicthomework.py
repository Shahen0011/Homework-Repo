# 1)Write a Python program to match key values in two dictionaries.
# Sample dictionary:dict_1= {'key1': 1, 'key2': 3, 'key3': 2},dict2 = {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both dict_1 and dict_2

# dic_1 = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year": 1964
# }

# dic_2 = {
#  "brand": "BMW",
#  "model": "E110",
#  "year": 1964
# }

# for x,i in dic_1.items():
# 	for y,j in dic_2.items():
# 		if x == y and i == j:
# 			print(x,i, f"is present in both {dic_1} and {dic_2} ")


# 2) Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

# this_dict = {
#  "brand": "Ford",
#  "model": "Mustang",
#  "year":None
# }


# d = {x:y for x,y in this_dict.items() if y != None}
# print(f"{this_dict} Dictionary \nwithout empty items ",d)


# 3)A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary.
# Original Dictionary:
# {'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# Update the list values of the said dictionary:
# {'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
	


# d1 = {
# 	"Math": [88,89,90],
# 	"Physics": [92,94,87],
# 	"Chemistry": [90,87,93]
# }

# for i in d1:
# 	if i == "Math":
# 		d1[i] = [89, 90, 91]
# 	elif i == "Physics":
# 		d1[i] = [90, 92, 87]
# 	elif i == "Chemistry":
# 		d1[i] = [90, 87, 93]
# print(d1)
		

# 4)Get a dictionary from 2 lists.

# keys = ["a","b","c"]
# values = [1,2,3]
# dic_1 = dict(zip(keys,values))
# print(f"This {dic_1} dictionary was gotten from \n {keys} and {values} lists ")


# 5) Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# n = int(input("Input number"))
# d1 = dict()

# for x in range(1, n + 1):
# 	d1[x] = x * x
# print(d1)


	
# 6)Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3

# dic_1 = {
# 	"Ararat": 3600,
# 	"Everest": 5000,
# 	"Aragats": 2000,
# 	"Hatis": 1000,
# 	"Sipan": 500
# }

# res = sorted(dic_1.values(),  reverse=True)[:3]
# for i in res:
# 	for x,y in dic_1.items():
# 		if i == y:
# 			print(x,y)


my_str = "I love my city, Erevan"
split_text  =my_str.split()
for i in split_text:
	dic1 = {i:len(i)}
	res = sorted(dic1.values(),  reverse=True)[:3]
	for i in res:
		for x,y in dic1.items():
			if i == y:
				print(x,y)



	
	


