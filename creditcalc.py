import math
import argparse

parser = argparse.ArgumentParser(description='Find out the missing parameter in the interest payment.')
parser.add_argument('-i', '--interest', help='Interest Percentage', default=0)
parser.add_argument('-m', '--periods', help='Number of months needed to repay the loan', default=0)
parser.add_argument('-P', '--principal', help='Principal amount', default=0)
parser.add_argument('-p', '--payment', help='Interest amount', default=0)
parser.add_argument('-t', '--type', help='Type of interest', default=0)

args = parser.parse_args()

def principal_calc(interest, periods, payment):
    n = int(periods)
    A = float(payment)
    i = float(interest)/1200.0

    Principal = A / ((i * (1 + i) ** n)/((1 + i) ** n - 1))
    return Principal

def periods_calc(interest, payment, principal):
    i = float(interest)/1200.0
    A = float(payment)
    P = float(principal)

    arg = A / (A - i * P)
    base = 1 + i
    n = math.log(arg, base)

    years = n // 12
    months = n % 12

    years = int(years)
    months = math.ceil(months)

    if months == 12:
        years += 1
        months = 0

    return years, months

def payment_calc(interest, principal, periods):
    i = float(interest)/1200.0
    P = float(principal)
    n = int(periods)

    Amount = P * ((i * (1 + i) ** n)/((1 + i) ** n - 1))
    total = math.ceil(Amount) * n
    return math.ceil(Amount), total

def annuity_calc():
    if args.periods == 0:
        Period = periods_calc(args.interest, args.payment, args.principal)
        if Period[0] == 0:
            print(f'It will take {Period[1]} months to repay this loan!')
            print(f"Overpayment = {math.ceil(float(args.payment))* Period[1] - int(args.principal)}")
        elif Period[1] == 0:
            print(f'It will take {Period[0]} years to repay this loan!')
            print(f"Overpayment = {math.ceil(float(args.payment)) * Period[0] * 12 - int(args.principal)}")
        else:
            print(f'It will take {Period[0]} years and {Period[1]} months to repay this loan!')
    elif args.principal == 0:
        Principal = principal_calc(args.interest, args.periods, args.payment)
        print(f'Your loan principal = {Principal}!')
    elif args.payment == 0:
        Amount = payment_calc(args.interest, args.principal, args.periods)
        print(f'Your monthly payment = {Amount[0]}!')
        print(f'Overpayment = {Amount[1] - int(args.principal)}')

def diff_calc():
    P = float(args.principal)
    i = float(args.interest)/1200.0
    n = int(args.periods)

    m = 0
    sum = 0
    for m in range(1, n + 1):
        D = P/n + i * (P - ((P * (m - 1))/n))
        D = math.ceil(D)
        sum += D
        print(f'Month {m}: payment is {D}')
    print(f"Overpayment = {sum - int(args.principal)}")


def args_counter():
    n = 0
    if args.interest != 0:
        n += 1
    if args.periods != 0:
        n += 1
    if args.payment != 0:
        n += 1
    if args.principal != 0:
        n += 1
    if args.type != 0:
        n += 1
    return n


numberofargs = args_counter()


if args.type != "annuity" and args.type != "diff":
    print("Incorrect parameters")
    # print("Here is the error1")

elif args.type == "diff" and round(float(args.payment)) != 0:
    print("Incorrect parameters")
    # print("Here is the error2")

elif numberofargs < 4:
    print("Incorrect parameters")
    # print("Here is the error3")
elif round(float(args.interest)) < 0 or int(args.periods) < 0 or int(args.principal) < 0 or int(args.payment) < 0:
    print("Incorrect parameters")
    # print("Here is the error4")
elif args.interest == 0:
    print("Incorrect parameters")
elif args.type == "diff":
    diff_calc()
else:
    annuity_calc()





# loan_principal = 'Loan principal: 1000'
# final_output = 'The loan has been repaid!'
# first_month = 'Month 1: repaid 250'
# second_month = 'Month 2: repaid 250'
# third_month = 'Month 3: repaid 500'
#
# # write your code here
# print(loan_principal, first_month, second_month, third_month, final_output, sep='\n')
#
# loan_amount = float(input("Enter the loan principal: "))
# calculation_type = input("""What do you want to calculate?
# type "m" - for number of monthly payments,
# type "p" - for the monthly payment: """)
# if calculation_type == "m":
#     monthly_payment = float(input("Enter the monthly payment: "))
#     no_of_months = round(loan_amount/monthly_payment)
#     if no_of_months == 1:
#         months = 'month'
#     else:
#         months = 'months'
#     print(f"It will take {no_of_months} {months} to repay the loan.")
# else:
#     number_of_months = int(input("Enter the number of months: "))
#     if loan_amount % number_of_months == 0:
#         monthly_payment = loan_amount/number_of_months
#         print(f"Your monthly payment = {monthly_payment}")
#     else:
#         monthly_payment = loan_amount/number_of_months
#         rounded_monthly_payment = math.floor(monthly_payment) + 1
#         last_month_payment = round(loan_amount - rounded_monthly_payment*(number_of_months - 1))
#         print(f"Your monthly payment = {rounded_monthly_payment} and the last payment = {last_month_payment}")
