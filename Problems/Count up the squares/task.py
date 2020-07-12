# put your python code here
numbers = []
sum_squares = 0

while True:
    user_input = int(input())
    numbers.append(user_input)
    if sum(numbers) == 0:
        for i in numbers:
            sum_squares += i ** 2
        print(sum_squares)
        break
