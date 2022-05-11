# 1)Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner,
#  and ask if the players want to start a new game)
#
# Remember the rules:
#
# Rock beats scissors
# Scissors beats paper
# Paper beats rock


# again = 'y'
# while again == 'y':
#     p1 = input("Player1 Choice rock,paper or scissors: ").lower()
#     p2 = input("Player2 Choice rock,paper or scissors: ").lower()
#     if p1 == "rock":
#         if p2 == "rock":
#             print("The game is a draw")
#         elif p2 == "paper":
#             print("Player 2 wins!")
#         elif p2 == "scissors":
#             print("Player 1 wins!")
#     elif p1 == "paper":
#         if p2 == "rock":
#             print("Player 1 wins!")
#         elif p2 == "paper":
#             print("The game is a draw")
#         elif p2 == "scissors":
#             print("Player 2 wins!")
#     elif p1 == "scissors":
#         if p2 == "rock":
#             print("Player 2 wins!")
#         elif p2 == "paper":
#             print("Player 1 wins!")
#         elif p2 == "scissors":
#             print("The game is a draw")
#     else:
#         print("Invalid input, try again")
#
#     again = input("Type y to play again, anything else to stop: ")

# 3)Use a dictionary comprehension to count the length of each word in inputed sentence.


# text = input("enter your string:")
# spl = text.split()
# result =  {i:len(i) for i in spl}
# print(f'Count the lenght of items in <<{text}>> ',result)

# 4)Get the factorial of number 6 using recursion.

# def fac_1(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac_1(n-1)
# print(fac_1(6),f'is The factorial of number 6 ')


# 5)Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function.
# Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
# Sum of the positive numbers: -32
# Sum of the negative numbers: 48

# result = sorted(l1, key = lambda i: 0 if i == 0 else -1 / i)

l1 = [2, 4, -6, -9, 11, -12, 14, -5, 17]
result = lambda n: n+=0 if n > 0 else n+=0 if n < 0
print(result(l1))














