a = int(input())
b = list(map(int, input().split()))
def neg(n):
    return n > 0
def odd(x):
    if x % 2 == 1:
        return x * 2
    else:
        return x
result = list((filter(neg, b)))
map_res= list(map(odd, b))
print(result)
print(map_res)