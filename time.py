import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

st = time.gmtime(timestamp)

print(time.asctime(st))
print(time.mktime((2019, 11, 4, 14, 53, 0, 0, 308, 0)))
print(time.asctime())

from datetime import datetime
dt=datetime(2020,11,4,14,53)
print(dt.strftime("%Y/%m/%d %X"))
print(dt.strftime("%y/%B/%d %H:%M:%S %p"))
print(dt.strftime("%a, %Y %b %d"))
print(dt.strftime("%A, %Y %B %d"))
print(dt.strftime("Weekday: %w"))
print(dt.strftime("Day of the year: %j"))
print(dt.strftime("Week number of the year: %W"))
