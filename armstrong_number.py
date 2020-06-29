"""
Armstrong Number
    Define a function that allows the user to check whether a given number is
    armstrong number or not.
    Hint: To do this, first determine the number of digits of the given number.
    Call that n. Then take every digit in the number and raise it to the nth
    power. Add them, and if your answer is the original number then it is an
    Armstrong number.
    Example: Take 1634.
    Four digits. So, 1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634.
    So 1634 is an Armstrong number.
    Tip: All single digit numbers are Armstrong numbers.
"""


def armstrong(my_number):
    number_string = str(my_number)  # Convert the number to a string to enable counting
    index = len(number_string)  # Find the length of the number and assign it to a variable
    total_sum = 0  # Variable to sum up the digits
    # Assign a new variable to my_number to work with without affecting the my_number variable
    number = my_number
    while number > 0:
        remainder = number % 10  # Splits the integer into its singular digits
        total_sum += remainder ** index  # Raises each digit to the power of the integer's length and adds them
        number //= 10  # Count the integer down to 0 or the while loop keeps going

    if my_number == total_sum:
        print(f'{my_number} is an Armstrong number')
    else:
        print(f'{my_number} is not an armstrong number')


armstrong(1634)
armstrong(153)
armstrong(9)
armstrong(121)
