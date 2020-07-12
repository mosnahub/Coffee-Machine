# put your python code here
numbers = []

while True:
    user_input = int(input())
    if user_input > 100:
        break
    numbers.append(user_input)

for i in numbers:
    if i < 10:
        continue
    print(i)
