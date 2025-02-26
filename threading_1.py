import threading
import time
from concurrent.futures import ThreadPoolExecutor

def func(seconds):
    print(f"Sleeping for {seconds} seconds")
    time.sleep(seconds)
    
# normal code
def main():
    time1 = time.perf_counter()
 # it will execute line by line and takes more time
# func(4)
# func(3)
# func(2)

# same code with threading
    t1= threading.Thread(target=func, args=[4])
    t2= threading.Thread(target=func, args=[3])
    t3= threading.Thread(target=func, args=[2])

    t1.start()
    t2.start()
    t3.start()

    t1.join
    t2.join
    t3.join

# calculating time    
    time2 =time.perf_counter()
    print(time2 - time1)
    
def poolingDemo():
    with ThreadPoolExecutor() as executor:
        future= executor.submit(func,3)
        print(future.result())
        future= executor.submit(func,4)
        print(future.result())
        future= executor.submit(func,5)
        print(future.result())
        
poolingDemo()
