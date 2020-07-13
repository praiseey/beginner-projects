import sys

"""
Pythagorean Triples Checker
    If you do not know how basic right triangles work, or what a Pythagorean
    Triple is read these articles on Wikipedia. Allows the user to input the
    sides of any triangle in any order. Return whether the triangle is a
    Pythagorean Triple or not.
    Loop the program so the user can use it more than once without having to
    restart the program.

Pythagoras Theorem:
The square of the hypothenuse is equal to the sum of the squares of the other two sides
"""


# def pythagorean_checker():


print()
print('PYTHAGOREAN TRIPLE CHECKER!!!')

while True:  # Keeps the entire program on a loop
    print('\nChoose an action:\nA. Check for Pythagorean Triples\nB. End Program')
    user_choice = input('>>> ').upper()

    while user_choice != 'A' and user_choice != 'B':
        print('Invalid option. Please try again.')
        user_choice = input('>>> ').upper()
    else:
        if user_choice == 'A':
            numbers = []  # Create a list to store the triples
            ''' Collect user input and add to list '''
            while True:
                try:
                    a = int(input('Enter the first number: '))
                except ValueError:
                    print('Invalid. Please enter a number')
                    a = int(input('Enter the first number: '))

                try:
                    b = int(input('Enter the second number: '))
                except ValueError:
                    print('Invalid. Please enter a number')
                    b = int(input('Enter the second number: '))

                try:
                    c = int(input('Enter the third number: '))
                except ValueError:
                    print('Invalid. Please enter a number')
                    c = int(input('Enter the third number: '))

                numbers.append(a)
                numbers.append(b)
                numbers.append(c)
                break
                # continue
            '''Arrange triples in ascending order and create a list to store them'''
            '''Find the square of each number'''
            sort = sorted(numbers)
            num_squared = []
            for num in sort:
                number = num ** 2
                num_squared.append(number)

            first_side = num_squared[0]
            second_side = num_squared[1]
            hypotenuse = num_squared[2]  # Hypotenuse is the longest side of a right-angled triangle
            add_sides = first_side + second_side

            if hypotenuse == add_sides:
                print(f'{numbers} is a pythagorean triple.')
            else:
                print(f'{numbers} is not a pythagorean triple')

        elif user_choice == 'B':
            sys.exit('Program Closed!')

