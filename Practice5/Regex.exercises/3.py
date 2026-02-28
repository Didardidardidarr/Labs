import re
a = input()
pat = re.compile(r"^[a-z]+[_]?$")
print(re.findall(pat, a))