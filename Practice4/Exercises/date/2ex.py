from datetime import datetime, timedelta
x = datetime.now()
yest = x - timedelta(days=1)
today = x
tom = x + timedelta(days=1)
print(yest)
print(today)
print(tom)