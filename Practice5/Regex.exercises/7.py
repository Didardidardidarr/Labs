import re
s = input().strip()
camel = re.sub(r'_([a-zA-Z])', lambda m: m.group(1).upper(), s)
print(camel)