from datetime import datetime, timedelta
a = input()
b = input()
date1 = datetime.strptime(a, "%Y-%m-%d %H:%M:%S.%f")
date2 = datetime.strptime(b, "%Y-%m-%d %H:%M:%S.%f")
minus = date2 - date1
sec = (minus.total_seconds())
print(int(sec))