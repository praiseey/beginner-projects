import sys

"""
Coin Estimator By Weight
    When some people receive change after shopping, they put it into a container and let it add up over time. Once they
    fill up the container, they'll roll them up in coin wrappers which can then be traded in at a bank for what they are
    worth. While most banks will give away coin wrappers for free, it's convenient to have an idea of how many you will
    need. Instead of counting how many coins you have, it's easier to separate all of your coins, weigh them, and then
    estimate how many of each type you have and then how many wrappers you'll need. For example, if you weigh all of
    your dimes and see that you have 1276.9g of them, you can estimate that you have about 563 dimes (since each one is
    2.268g) and you would be able to fill 11 dime wrappers.
    Here is the weight of each coin and how many fit inside each type of wrapper.
    Allow the user to input the total weight of each type of coin they have (pennies, nickels, dimes, and quarters).
    Print out how many of each type of coin wrapper they would need, how many coins they have, and the estimated total
    value of all of their money.
    Subgoals:
    Round all numbers printed out to the nearest whole number.
    Allow the user to select whether they want to submit the weight in either grams or pounds.

"""
print()
print('TRADE IN YOUR COINS')

while True:  # Keeps the program on a loop
    print('\nWhat would you like to do?')
    user_choice = input('A. Trade Coins\nB. Close Program\nChoose an action(A-B): ').upper()
    print()

    '''Use a while loop to check when a user enters an invalid option'''
    while user_choice != 'A' and user_choice != 'B':
        print('Invalid option. Please try again.')
        user_choice = input('>>> ').upper()

    else:
        if user_choice == 'A':  # User wants to trade coins
            print('A. Pennies\nB. Nickels\nC. Dimes\nD. Quarters')
            coin_type = input('What type of coins?(A - D): ').upper()
            while coin_type != 'A' and coin_type != 'B' and coin_type != 'C' and coin_type != 'D':
                print('Please choose a valid option.')
                coin_type = input('>>> ').upper()
            else:
                while True:
                    try:
                        total_weight = float(input('Total weight of your coins: '))
                    except ValueError:
                        print('Invalid value. Please enter a number.')
                        total_weight = float(input('>>> '))
                    print()
                    break

                weight_unit = input('Are you weighing in pounds(lbs) or grams(g)?\nA.(lbs)\nB.(g)\n>>> ').upper()
                while weight_unit != 'A' and weight_unit != 'B':
                    print('Invalid option. Please try again.')
                    weight_unit = input('>> ').upper()
                else:
                    if weight_unit == 'A':  # If user's total coin weight is in pounds
                        if coin_type == 'A':
                            number_of_pennies = round(total_weight / 0.0055)
                            penny_wrappers = round(number_of_pennies / 50)
                            dollars = round(number_of_pennies / 100)
                            print(f'You have {number_of_pennies} pennies.\nYou need {penny_wrappers} penny wrappers.\n'
                                  f'Estimated Value: ${dollars}')
                        elif coin_type == 'B':
                            number_of_nickels = round(total_weight / 0.0110)
                            nickel_wrappers = round(number_of_nickels / 50)
                            dollars = round(number_of_nickels / 20)
                            print(f'You have {number_of_nickels} nickels.\nYou need {nickel_wrappers} nickel wrappers.\n'
                                  f'Estimated Value: ${dollars}')

                        elif coin_type == 'C':
                            number_of_dimes = round(total_weight / 0.0050)
                            dime_wrappers = round(number_of_dimes / 50)
                            dollars = round(number_of_dimes / 10)
                            print(f'You have {number_of_dimes} nickels.\nYou need {dime_wrappers} dime wrappers.\n'
                                  f'Estimated Value: ${dollars}')

                        elif coin_type == 'D':
                            number_of_quarters = round(total_weight / 0.0125)
                            quarter_wrappers = round(number_of_quarters / 50)
                            dollars = round(number_of_quarters)
                            print(f'You have {number_of_quarters} nickels.\nYou need {quarter_wrappers}quarter wrappers.\n'
                                  f'Estimated Value: ${dollars}')

                    elif weight_unit == 'B':  # If user's total coin weight is in grams
                        if coin_type == 'A':
                            number_of_pennies = round(total_weight / 2.500)
                            penny_wrappers = round(number_of_pennies / 50)
                            dollars = round(number_of_pennies / 100)
                            print(f'You have {number_of_pennies} pennies.\nYou need {penny_wrappers} penny wrappers.\n'
                                  f'Estimated Value: ${dollars}')
                        elif coin_type == 'B':
                            number_of_nickels = round(total_weight / 5.000)
                            nickel_wrappers = round(number_of_nickels / 50)
                            dollars = round(number_of_nickels / 20)
                            print(f'You have {number_of_nickels} nickels.\nYou need {nickel_wrappers} nickel wrappers.\n'
                                  f'Estimated Value: ${dollars}')

                        elif coin_type == 'C':
                            number_of_dimes = round(total_weight / 2.268)
                            dime_wrappers = round(number_of_dimes / 50)
                            dollars = round(number_of_dimes / 10)
                            print(f'You have {number_of_dimes} nickels.\nYou need {dime_wrappers} dime wrappers.\n'
                                  f'Estimated Value: ${dollars}')

                        elif coin_type == 'D':
                            number_of_quarters = round(total_weight / 5.670)
                            quarter_wrappers = round(number_of_quarters / 50)
                            dollars = round(number_of_quarters)
                            print(f'You have {number_of_quarters} nickels.\nYou need {quarter_wrappers}quarter wrappers.\n'
                                  f'Estimated Value: ${dollars}')

        elif user_choice == 'B':  # User wants to close the program.
            sys.exit('Program cosed!')
