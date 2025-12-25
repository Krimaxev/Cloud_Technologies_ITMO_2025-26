import time

a = bin(10**1000)[2:]
for i in range(100):
    str_a = str(a)
    s = str_a.replace('0','X').replace('1','O')
    print(s)
    time.sleep(1)
