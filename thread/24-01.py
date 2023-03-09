"""
THREAD
part of a program or lightweight process
2 types- single anf multithreading
"""

# from time import sleep
# def task():
#     sleep(3)
#     print("this is from another thread ")
#
# # task()
#
# from threading import Thread
#
# #create a thread
# thread = Thread(target=task)
#
# #Next, we can create an instance of the threading.Thread class and specify
# # our function name as the "target" argument in the constructor.
# # run the thread
# thread.start()
# #The start() function does not block, meaning it returns immediately.


""" WITH ARGUMENT """
from time import sleep
def task(sleep_time, message):
# block for a moment
 sleep(sleep_time)
 # display a message
 print(message)


from threading import Thread
#create a thread
thread= Thread(target=task, args=(1.5," New message from another thread"))
#run the thread
thread.start()

# wait for the thread to finish

print('Waiting for the thread...')
thread.join()


