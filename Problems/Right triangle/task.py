class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.area = 0.5 * leg_1 * leg_2


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
r_t = RightTriangle(input_c, input_a, input_b)

if (r_t.c ** 2) == ((r_t.a ** 2) + (r_t.b ** 2)):
    print(r_t.area)
else:
    print("Not right")
