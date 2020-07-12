# put your python code here
a, b = int(input()), int(input())
sum_, count = 0, 0

for i in range(a, b + 1):
    if i == 0 or i % 3 == 0:
        sum_ += i
        count += 1

print(sum_ / count)
