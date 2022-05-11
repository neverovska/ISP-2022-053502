import math
some_list = ["one", 2, 2.25, "five", True, None]
some_dict = {"one": 1, 2: "two", "three": "3", 4: 4.0}


def inc(n):
    return n + 1


def fibonacci(n):
    cur = 1
    if n > 2:
        cur = fibonacci(n - 1) + fibonacci(n - 2)
    return cur


c = 42


class Testsik:
    def prin(self):
        print("hello")


testsuka = Testsik()

def f(x):
    a = 123
    return math.sin(x * a * c)
