import time

a = bin(10**1000)[2:]
for i in range(100):
    print(str(a))
    time.sleep(1)