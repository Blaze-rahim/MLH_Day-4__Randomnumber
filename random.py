import time

data = str(time.time())
lst = list(data.split("."))
strr = int(lst[1])#taking after decimal part
a = len(lst[1])-1
divider = int("1" + ("0"*a))
result = strr//divider
print(result)
