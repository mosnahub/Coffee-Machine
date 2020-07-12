# put your python code here
a = float(input())
b = float(input())
operator = input()

if operator == '+':
    print(a + b)
elif operator == '-':
    print(a - b)
elif operator == '*':
    print(a * b)
elif operator == '/':
    print("Division by 0!" if b == 0 else a / b)
elif operator == 'mod':
    print("Division by 0!" if b == 0 else a % b)
elif operator == 'pow':
    print(1 if b == 0 else a ** b)
elif operator == 'div':
    print("Division by 0!" if b == 0 else a // b)
