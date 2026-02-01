a = 15
while a >= 0:
    print(a)
    a = a - 1



a = int(input())
while a < 10:
    if(a == 5):
        break
    else:
        print(a)
    a = a + 1



a = int(input())
while a < 15:
    a = a + 1
    if(a % 2 == 0):
        continue
    else:
        print(a)   



a = int(input())
while a % 1 == -1:
    print(a)
    a = a + 1
