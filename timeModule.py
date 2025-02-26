import time

# time.time() method
# def usingWhile():
#     i=0
#     while(i<500):
#         print(i)
#         i=i+1

# def usingFor():
#     for i in range(500):
#         print(i)
        
# init= time.time()
# usingFor()
# t1= time.time()- init
# init= time.time()
# usingWhile()
# print(time.time()- init)
# print(t1)

# sleep() method
# print(4)
# time.sleep(3)
# print("this is executed after 3 seconds.")

# time.strftime() method

t= time.localtime()
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S",t)
print(formatted_time)
        
    