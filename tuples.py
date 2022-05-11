# myTuple = (1,"Apple",True)
# myTuple[0] = "bananas"
# print(myTuple)

# myList = [1, "apple", True]
# mytuple = tuple(myList)
# print(mytuple)


# thistuple = ("apple",)
# print(type(thistuple))


#1

# myTuple = (10, 20, 30, 40, 50)
# srot_tup = sorted(myTuple, reverse = True)
# print(srot_tup)


#2  

# my_tup =  ("Orange", [10, 20, 30], (5, 15, 25))
# print(my_tup[1][1])

#3

# tuple1 = (11, 22, 33, 44, 55, 66)
# for i in l1:
# 	if i == 44 and i == 55:
# 		print(i)

#4

# tuple1 = (50, 10, 60, 70, 50)
# amount = 0
# for i in tuple1:
# 	if i == 50:
# 		amount += 1
# print(amount)


# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}



# set3 = set1.union(set2)
# print(set3)
# print(set3)



#Sets exercises


#1

# my_str = input("Enter")
# my_st = set(my_str)
# print(my_st)

#2 

l1 = [1,2,3]
l2 = [4,2,5]
l3 = [6,7,2]

j_l = l1 + l2 + l3
my_set = set(j_l)
for i in my_set:
	for x in my_set:
		if i == x:
			print(i,x)


