N = int(input())
square = (x*x for x in range(1, N))
for i in square:
    print(i, end=" ")