from datetime import datetime, timedelta
x = input()
date = datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f")
drop = date.replace(microsecond=0)
print(drop)