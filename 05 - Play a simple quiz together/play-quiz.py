# Objective
# Your bot can ask anything you want, but there are two rules for your output:
# - the line with the test should end with the question mark character;
# - an option starts with a digit followed by the dot (1., 2., 3., 4.)

# If a user enters an incorrect answer, the bot may print a message:
# 'Please, try again.'

# The program should stop on the correct answer and print 'Congratulations, have a nice day!' at the end.

def test():
    print("Let's test your programming knowledge.")
    print("Why do we use methods?")
    print("1. To repeat a statement multiple times.")
    print("2. To decompose a program into several small subroutines.")
    print("3. To determine the execution time of a program.")
    print("4. To interrupt the execution of a program.")

    answer = int(input())
    while answer != 2:
        print("Please try again.")
        answer = int(input())

    print('Completed, have a nice day!')


test()
print('Congratulations, have a nice day!')