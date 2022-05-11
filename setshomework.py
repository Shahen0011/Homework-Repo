# 1)Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order. 


my_str = input("Enter your sentence")
frag =  my_str.split()
result = frag[::-1]
print(f"This is your sentence upside down  ")
print(" ".join(result))


# 2) You, the user, will have in your head a number between 0 and 100.
#  The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.



# num = range(100)
# print("If your secret number is 50, input c, if 50 is high input h if low input l")
# my_str = input("Your answeer")
# while True:
# 	if my_str == "c":
# 		break
# 	elif my_str == "h":
		

	
