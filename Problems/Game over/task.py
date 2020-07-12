scores = input().split()
# put your python code here
count, incorrect = 0, 0
for i in scores:
    if i == 'I':
        incorrect += 1
        if incorrect == 3:
            print("Game over")
            print(count)
            break
    elif i == 'C':
        count += 1

if incorrect < 3:
    print(f"You won\n{count}")
