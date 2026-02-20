def generator(n):
    num = (x for x in range(0, n))
    for i in num:
        if i % 3 == 0 or i % 4 == 0:
            print(i, end=" ")
N = int(input())
generator(N)