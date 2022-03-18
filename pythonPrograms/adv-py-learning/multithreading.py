import threading
import time

def hello():
    for i in range(5):
        print("Hello ")
        time.sleep(1)
def hi():
    for i in range(5):
        print("Hi")
        time.sleep(1)


hello_thread = threading.Thread(target=hello)

hi_thread = threading.Thread(target=hi)
hello_thread.start()
hi_thread.start()