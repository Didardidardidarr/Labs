x = lambda a : a + 10
print(x(10))



def function(n):
    return lambda a:a*n
res = function(15)
print(res(15))



numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)



numbers = [1, 2, 3, 4, 5, 6]
even=list(filter(lambda x:x % 2 == 0, numbers))
print(even)



sttuddents = [("Dias", 18), ("Temirlan", 17)]
sortted = sorted(sttuddents, key=lambda x:x[1])
print(sortted)