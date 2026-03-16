a = input().split()
age = list(map(int, input().split()))
names = input().split()
for i,value in enumerate(a):
    print(f"{i}: {value}", end=" ")
for ages,namess in zip(age,names):
    print(f"{ages}: {namess}", end=" ")