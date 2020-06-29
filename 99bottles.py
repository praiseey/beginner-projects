"""
99 BOTTLES
    Create a program that prints out every line to the song "99 bottles of beer on the wall."
    Do not use a list for all of the numbers, and do not manually type them all in. Use a built in function instead.
    Besides the phrase "take one down," you may not type in any numbers/names of numbers directly into your song lyrics.
    Remember, when you reach 1 bottle left, the word "bottles" becomes singular.

    Song lyrics:
    99 bottles of beer on the wall. Take one down, pass it around. 98 bottles of beer on the wall.
"""

print('99 bottles of beer on the wall. Take one down, pass it around. 98 bottles of beer on the wall.')
number_of_bottles = 99
remaining_bottles = 98
for bottles in range(1, 99):
    while 99 >= number_of_bottles > 1:
        number_of_bottles -= 1
        remaining_bottles -= 1

        if number_of_bottles == 1:
            print(f'{number_of_bottles} bottle of beer on the wall, {number_of_bottles} bottle of beer. '
                  f'\nTake one down and pass it around, No more bottles of beer on the wall.')

        elif remaining_bottles == 1:
            print(f'{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer. '
                  f'\nTake one down and pass it around, {remaining_bottles} bottle of beer on the wall.')
            print()

        else:
            print(f'{number_of_bottles} bottles of beer on the wall, {number_of_bottles} bottles of beer. '
                  f'\nTake one down and pass it around, {remaining_bottles} bottles of beer on the wall.')
            print()
