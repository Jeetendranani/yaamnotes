# hello_python_with_threads.py
# To use threads you need import the Tread using the following code:


from threading import Thread
# Also we use time sleep function to make the thread "sleep"
from time import sleep


# to create a thread in python you'll want to make your class work as a thread.
# For this, you should subclass your class from teh Threed class.
class CookBook(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.message = "Hellow Parallel Python Cookbook!!\n"

    # this method prints only the message
    def print_message(self):
        print(self.message)

    # the run method prints ten times the message
    def run(self):
        print("Thread starting\n")
        x = 0
        while x < 10:
            self.print_message()
            sleep(2)
            x += 1
        print("Thread Ended")


# start the main process
print("Process Started")

# create an instance of the Hello World class
hello_python = CookBook()

# print the message ... starting the thread
hello_python.start()

hello_python.join()

# end the main process
print("Process Ended")