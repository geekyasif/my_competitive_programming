import time
from functools import lru_cache

#------------------------------function caching----------------------
#function caching is a teqnique to call the function at first time with a time interval and then store in chache memory
# after when we the function again it doest take given time it call imidieatly

#maxsize - takes number of latest time to store in a function ...it takes all the time at once and store in chache memory
@lru_cache(maxsize=4)
def func(n):
    time.sleep(n)
    return "this is a function caching with the help of lru_chace"

if __name__ == '__main__':
    print("Function calling..........")
    #it takes given secs and then call
    func(3)
    print("Done....calling again")
    # it doesn't take time because it already store in chache memory
    func(3)
    print("Done")