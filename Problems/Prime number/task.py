number = int(input())
count = 0

for i in range(1, number):
    if number % i == 0:
        count += 1


if count > 1 or (number == 1):
    print("This number is not prime")
else:
    print("This number is prime")
