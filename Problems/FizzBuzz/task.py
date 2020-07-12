for i in range(1, 101):
    o = ""
    if i % 3 == 0:
        o += 'Fizz'
    if i % 5 == 0:
        o += 'Buzz'

    print(o or i)
