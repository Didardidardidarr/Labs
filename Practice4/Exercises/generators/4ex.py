def function(n):
    while n >= 0:
        yield n
        n = n - 1
n = int(input())
ctr = function(n)
for i in ctr:
    print(i, end=" ")        