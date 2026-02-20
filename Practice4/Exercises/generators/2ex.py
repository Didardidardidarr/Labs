n = int(input())
even = (x for x in range(1, n))
for i in even:
    if i % 2 == 0:
        print(i, end=" ")    