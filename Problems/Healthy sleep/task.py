a = int(input())
b = int(input())
h = int(input())

if a <= h <= b:
    print("Normal")
elif a <= b <= h:
    print("Excess")
else:
    print("Deficiency")
