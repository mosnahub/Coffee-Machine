score = int(input())
max_ = int(input())

if score >= (max_ * 0.9):
    print('A')
elif score >= (max_ * 0.8):
    print('B')
elif score >= (max_ * 0.7):
    print('C')
elif score >= (max_ * 0.6):
    print('D')
else:
    print('F')
