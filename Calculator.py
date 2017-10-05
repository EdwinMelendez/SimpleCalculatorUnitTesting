import math

class calc:

    def add(self, a, b):
        ans_add = a + b
        print('Answer: ' + str(ans_add) + '\n')

    def sub(self, a, b):
        ans_sub = a - b
        print('Answer: ' + str(ans_sub) + '\n')

    def mult(self, a, b):
        ans_mult = a * b
        print('Answer: ' + str(ans_mult) + '\n')

    def div(self, a, b):
        ans_div = a / b
        print('Answer: ' + str(ans_div) + '\n')

    def square(self, a):
        ans_sq = math.sqrt(a)
        print('Answer: ' + str(ans_sq) + '\n')
