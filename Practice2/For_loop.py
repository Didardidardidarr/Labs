a = int(input())
for i in range(a):
    print(i)



a = int(input())
sum = 0
for i in range(a):
    sum = i + sum
print(sum)



a = ["abc", "efg", "hij"]
for i in a:
    print(i)



a = int(input())
array = list(map(int, input().split()))
for i in array:
    if i % 2 == 0:
        print(i, end=" ")



for i in range(2, 6):
    print(i)