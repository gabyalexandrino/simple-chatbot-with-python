# Objective
# In this stage, you will program the bot to count from 0 to any positive number users enter.
# Note: each number starts with a new line, and after a number, the bot should print the exclamation mark.

# Using a consistent type of quotation marks (either single ' or double " quotes) in your code enhances readability and reduces the chances of syntax errors. Consistency also makes it easier to follow coding standards, especially when collaborating with others, ensuring that the code remains clean and professional.
print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

rem3 = int(input())
rem5 = int(input())
rem7 = int(input())

age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

print("Your age is " + str(age) + "; that's a good time to start programming!")
print('Now I will prove to you that I can count to any number you want.')
number = int(input())
count = 0
while count <= number:
    print(f"{count} !")
    count += 1

print('Completed, have a nice day!')
