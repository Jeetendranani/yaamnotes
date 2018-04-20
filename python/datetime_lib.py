from datetime import datetime


now = datetime.now()
print(now)

print(type(now))

dt = datetime(2018, 4, 20, 17, 10)
print(dt)
print(dt.timestamp())

t = 1524269400.0
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

print(now.strftime('%a, %b, %d, %H:%M'))