from functools import reduce
def fun(x,y):
    return x*y
a = int(input())
b = list(map(int, input().split()))
result = reduce(fun, b)
print(result)