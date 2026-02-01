a = 12
if a == 12:
    print("a equals 12!")



a = "string"
if len(a) % 2 == 0:
    print("Length of a is even")
else:
    print("Length of a is odd")



a = int(input())
b = int(input())
if a > b: print("a is greater than b")



a = int(input())
b = int(input())
print(a) if a > b else print(b)



a = input()
b = input()
if len(a) % 2 == 0 and len(b) % 2 == 0:
    print("Length of a and b are even")



a = int(input())
while a < 0:
    print(a)
    a = a + 1



a = int(input())
while a < 10:
    print(a)
    a = a + 1
else:
    print(a, "is not less than 10")    