import calendar
import time
print(calendar.month(2020,1))
print(calendar.calendar(2020))
print(calendar.isleap(2100))
print(calendar.leapdays(2020,2030))
# https://www.programiz.com/python-programming/datetime




# time in sec since 1970
print(time.time())

print(time.localtime(time.time()))

print(time.asctime(time.localtime(time.time())))