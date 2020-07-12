numbers = []

while True:
    input_ = input()
    if input_ == '.':
        break
    numbers.append(float(input_))

print(min(numbers))
