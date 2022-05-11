# 1)Write a Python program to get a string from a given string where all occurrences of its "r" char have been changed to '$'.

# print("All r in your string will change to $")
# my_str = input("Enter the string")
# x = my_str.replace("r", "$")
# print(x)

# 2)Write a Python program to swap comma and dot in a string. 
# Sample string: "32.054,23"
# Expected Output: "32,054.23"

# print("(,)the sign will change (.) and the opposite")

# amount = input("Enter your string")
# maketrans = amount.maketrans
# amount = amount.translate(maketrans(',.', '.,'))
# print(amount)
		




# 3) Write a Python program to compute sum of digits of a given string

# inputstr = input("Enter your string: ")
# sum_total = 0
# for x in inputstr:
#     if x.isdigit():
#         sum_total += int(x)
# print("Sum of al digits in your string")
# print(sum_total)


# 4)Write a Python program to remove spaces from a inputed sentence.

# new_string = input("Enter your string")
# without_spaces = new_string.replace(" ","")
# print("This is your string without spaces")
# print(without_spaces)


# 5)Write python program to print even length words from inputed sentence.

# your_str = input("Enter your string:")
# even = your_str.split()
# print("This are even lenght words \nfrom your strng and their lenght \n")
# for i in even:
# 	if len(i) % 2 == 0:
# 		print(i, "--------", len(i), "Lenght of words")


# 6) Write a program to count how many letters and numbers are in given word

# num = 0
# let = 0

# my_str = input("Enter the word:")
# for i in my_str:
# 	if i.isdigit():
# 		num += 1
# 	elif i.isalpha():
# 		let += 1

# print("In imputted word number of dgits are",num)
# print("In inputted word number of letters are",let)

# 7)Write a Python program to count the number of characters (character frequency) in a string

# print("The frequency of  characters ")

# my_str = input("Enter your word:")
# for i in my_str:
# 	print(i, my_str.count(i), "times")

# 8) Write a Python script that takes input from the user and displays that input back in upper and lower cases. 

# my_str = input("Enter word")
# print("These are uppercases")
# for i in my_str:
# 	if i.isupper():		
# 		print(i)
# print("These are lowercases")		
# for x in my_str:
# 	if x.islower():
# 		print(x)		


# 9)Write a Python script that has a list and convert into comma separated string.
# Sample list:['Geeks', 'for', 'Geeks']
# output:Geeks-for-Geeks

# l1 = input("Enter your string")
# x = l1.split()
# total = "-".join(x)
# print(total)

# 10) Python program to convert  starting letter of a word in upper case format or in the title format.
# sample list

# my_str = input("Enter you string")
# x = my_str.split()
# total = " ".join(x)
# print(total.title())
			
		