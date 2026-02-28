import re
a = input()
pat = re.compile(r"[.,\s]+")
rep = re.sub(pat, ":", a)
print(rep)