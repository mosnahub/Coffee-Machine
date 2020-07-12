lines = int(input())
arr = []

for a in range(lines):
    numbers = int(input())
    if numbers % 7 == 0 or numbers == 0:
        arr.append(numbers ** 2)

for i in arr:
    print(i)
