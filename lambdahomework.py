#1)Use the sorted() function to sort the list in ascending order with lambda.


# l1 = ['1', '6', '5', '7', '3', '9']
# sorted_list = sorted(l1, key=lambda x: int(x[0:]))
# print("The list of sorted values are")
# for i in sorted_list:
#     print(i, end=',' )


# 2) Write a Python program to sort each sublist of strings in a given list of lists using lambda.
# Original list using lambda:
# [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# After sorting each sublist of the said list of lists:
# [['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


# my_list =  [['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
# result = [sorted(x, key= lambda x:x[0]) for x in my_list]
# print(list(result))

# 3)Write a Python program to count float number in a given mixed list using lambda.
# Original list:
# [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]


# l1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# result = filter(lambda x: isinstance(x,float),l1)
# print(len(list(result)), f"Is The number of floats number in {l1} list ")

# 4)Write a Python program to count the occurrences of the items in a given list using lambda. Go to the editor
# Original list:
# [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# Count the occurrences of the items in the said list:
# {3: 4, 4: 2, 5: 3, 8: 2, 0: 2, 1: 1, 2: 2}

# l1 =  [3, 4, 5, 8, 0, 3, 8, 5, 0, 3, 1, 5, 2, 3, 4, 2]
# resullt = dict(map(lambda x: (x, list(l1).count(x)), l1))
# print(resullt, f"Count the occurrences of the items in the \n{l1} list ")


# 5)Write a Python program to remove None value from a given list using lambda function. Go to the editor
# Original list:
# [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# Remove None value from the said list:
# [12, 0, 23, -55, 234, 89, 0, 6, -12]


# l1 = [12, 0, None, 23, None, -55, 234, 89, None, 0, 6, -12]
# result = filter(lambda x: x != None,l1)
# print(list(result))

# 6)  Write a Python program to check whether a given string is number or not using Lambda.
# Sample Output:
# True
# True
# False
# True


# my_str = input("Enter your string")
# result = map(lambda x: x.isdigit(), my_str)
# print("If program return True, it`s mean that items from your inputted string is number, \nif return False, items is not number")
# print(list(result))

# 7)Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
# Original arrays:
# [-1, 2, -3, 5, 7, 8, 9, -10]
# Rearrange positive and negative numbers of the said array:
# [2, 5, 7, 8, 9, -10, -3, -1]



# l1 = [-1, 2, -3, 5, 7, 8, 9, -10]
# result = sorted(l1, key = lambda i: 0 if i == 0 else -1 / i)
# print(result, f"Rearrange positive and negative numbers of the {l1} ")


