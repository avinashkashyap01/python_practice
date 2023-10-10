
# Processes

from multiprocess import Process
import time

def longsquare(num, results):
    time.sleep(1)
    results[num] = num**2
    print("Finished Computing!!!")

results = {}

p1 = Process(target=longsquare, args=(1,results))
p2 = Process(target=longsquare, args=(2,results))

p1.start()
p2.start()

p1.join()
p2.join()

print(results)




# def longsquare(num,results):
#     time.sleep(1)
#     print(num**2)
#     print('finished computing!')
#
# results = { }
# processes = [process(target=longsquare,args=(n,results)) for n in range(0,10)]
# print([p.start() for p in processes])
# print([p.join() for p in processes])
