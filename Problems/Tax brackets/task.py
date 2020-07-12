income = int(input())


def print_tax(income_, percent):
    calculated_tax = income_ * (percent / 100)
    print(f"The tax for {income_} is {percent}%. That is {int(round(calculated_tax))} dollars!")


if income < 15528:
    print_tax(income, 0)
elif income < 42708:
    print_tax(income, 15)
elif income < 132407:
    print_tax(income, 25)
else:
    print_tax(income, 28)
