# Objective
# In this stage, you will introduce yourself to the bot. It will greet you by your name and then try to guess your age using arithmetic operations.
# Your program should print the following lines:

# Hello! My name is Aid.
# I was created in 2023.
# Please, remind me your name.
# What a great name you have, Max!
# Let me guess your age.
# Enter remainders of dividing your age by 3, 5 and 7.
# Your age is {your_age}; that's a good time to start programming!

# Read three numbers from the standard input. Assume that all the numbers will be given on separate lines.
# Instead of {your_age}, the bot will print the age determined according to the special formula discussed above.

print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

remainder3 = int(input())
remainder5 = int(input())
remainder7 = int(input())
your_age = (remainder3 * 70 + remainder5 * 21 + remainder7 * 15) % 105

print(f"Your age is {your_age}; that's a good time to start programming!")
