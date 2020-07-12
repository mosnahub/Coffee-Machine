cafe = []
cats = []

while True:
    user_input = input().split()
    # print(user_input)
    if 'MEOW' in user_input:
        break
    cafe.append(user_input[0])
    cats.append(int(user_input[1]))
    # print(cafe)
    # print(cats)

print(cafe[cats.index(max(cats))])
