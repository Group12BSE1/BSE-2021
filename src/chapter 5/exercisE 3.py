nickels = 25
dimes = 25
quarters = 25
one_dollar = 0
five_dollar = 0


def menu_message():
    print('MENU FOR DEPOSITS')
    print('n -- deposit a nickel')
    print('d -- deposit a dime')
    print('q -- deposit a quarter')
    print('o -- deposit a one dollar bill')
    print('f -- deposit a five dollar bill')
    print('c -- caancel the deposit')


def stock_contains(n_value, d_value, q_value, o_value, f_value):
    print(f'{n_value} nickels')
    print(f'{d_value} dimes')
    print(f'{q_value} quarter')
    print(f'{o_value} one dollar bill')
    print(f'{f_value} five dollar bill')


def testUserInput(value):
    status = ''
    dollar = value // 1
    cents = value % 1
    finalCents = round(cents, 2)
    centsToFull_digit = finalCents * 100
    totalCents = (dollar * 100) + round(centsToFull_digit)
    if (totalCents % 5) == 0 and totalCents >= 0:
        status = 'YES'
    else:
        status = 'NO'
    return status


print("Welcome to the vending machine change maker program \n Change maker initialized")
stock_contains(nickels, dimes, quarters, one_dollar, five_dollar)
AmountToPay = float(input("Enter the purchase price (xx.xx) or 'q' to quit: "))
status = testUserInput(AmountToPay)
if status == "YES":









