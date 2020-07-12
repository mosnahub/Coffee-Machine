x = []

while True:
    user_input = input()
    if user_input == '.':
        break
    x.append(int(user_input))


print(sum(x) / len(x))
