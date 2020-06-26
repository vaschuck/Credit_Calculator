from math import ceil
print('Enter the credit principal')
credit_principal = int(input())
print('What do you want to calculate?')
print('type "m" = for count of months,')
print('type "p" = for monthly payment:')
choice = input()

if choice == 'm':
    monthly_payment = int(input())
    months = ceil(credit_principal / monthly_payment)
    if months == 1:
        print(f'It takes {months} month to repay the credit')
    else:
        print(f'It takes {months} months to repay the credit')
else:
    months = int(input())
    monthly_payment = ceil(credit_principal / months)
    last_payment = ceil(credit_principal - (months - 1) * monthly_payment)
    if monthly_payment != last_payment:
        print(f'Your monthly payment = {monthly_payment} with last month payment = {last_payment}')
    print(f'Your monthly payment = {monthly_payment}')
