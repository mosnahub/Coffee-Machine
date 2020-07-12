name_list = []

while True:
    user_input = input()
    if user_input == '.':
        break
    else:
        name_list.append(user_input)


print(name_list)
print(len(name_list))
