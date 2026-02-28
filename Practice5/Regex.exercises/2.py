import re
a = input()
pat = re.compile(r"^[a]b{2,3}$")
print(re.match(pat, a))