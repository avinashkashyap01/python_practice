

# Threads

import threading
import time

def longsquare(num):
    time.sleep(1)
    return num**2
print([longsquare(n) for n in range(0,5)])



def longsquare(num,results):
    time.sleep(1)
    results[num] = num**2

results = {}
t1 = threading.Thread(target=longsquare, args=(1,results))
t2 = threading.Thread(target=longsquare, args=(2,results))

t1.start()
t2.start()

t1.join()
t2.join()

print(results)




def longsquare(num,results):
    time.sleep(1)
    results[num] = num**2

results = { }
threads = [threading.Thread(target=longsquare,args=(n,results)) for n in range(0,100)]
[t.start() for t in threads]
[t.join() for t in threads]
print(results)
