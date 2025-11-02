# # 1. Even or Odd
# # Write a Python program that asks the user for a number and prints whether it’s even or odd.

# user_numb = input(f"Please enter a number to check if the number is a odd or even number: \n")

# user_numb_int = int(user_numb)

# if user_numb_int % 2 == 0:
#     user_numb_int = "Even"
# else:
#     user_numb_int = "Odd"

# print(f"The number you have entered is: {user_numb_int}!")

# # ----------------------------------------------------------

# # 2. Simple Calculator
# # Ask the user to input two numbers and an operator (+, -, *, or /).
# # Then, display the result based on the operator entered.

# print(f"Please enter 2 numbers and one of these operators (+, -, *, or /) to calculate the result.")

# user_calc_1 = input(f"Please enter the first number: \n")
# user_calc_op = input(f"Please enter a Operator out of these (+, -, *, or /): \n")
# user_calc_2 = input(f"Please enter the second number: \n")

# answer_numb_1 = int(user_calc_1)
# answer_numb_2 = int(user_calc_2)

# if user_calc_op == "+":
#     answer  = answer_numb_1 + answer_numb_2
# if user_calc_op == "-":
#     answer = answer_numb_1 - answer_numb_2
# if user_calc_op == "*":
#     answer = answer_numb_1 * answer_numb_2
# if user_calc_op == "/":
#     answer = answer_numb_1 // answer_numb_2


# print(f"The answer is: {answer}!")


# # ----------------------------------------------------------

# # 3. Count Vowels
# # Ask the user to enter a word or sentence, and count how many vowels (a, e, i, o, u) it contains.

# user_answer = input(f"Please enter a word to count how many vowels it contains: \n")

# vowels_list = ["a", "e", "i", "o", "u"]

# if vowels_list in user_answer:
#     vowel_count = user_answer(len(vowels_list))

# if vowel_count == 1:
#     print(f"Your entered word has: 1 vowel")
# else:
#     print(f"Your entered word has:{vowel_count} vowels")



# correcting the excises after this


# 1. Even or Odd
# Write a Python program that asks the user for a number and prints whether it’s even or odd.

user_answer = int(input(f"Please enter a number to check if it's an odd or even number: \n"))

if user_answer % 2 == 0:
    result = "even"
else:
    result = "odd"


print(f"The number you have entered is a {result} number!")

