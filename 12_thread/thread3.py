import threading
from time import sleep
from  random import randint

condtion_value = 0

def worker(lock,id,value,condtion):
    global condtion_value
    with lock:
        print("{} thread acqured lock".format(id))
        print("Will sleep for {}".format(value))
        sleep(value)
        condtion_value = condtion_value + 1
        if condtion_value == 10:
            print("Last one. Notifying main")
            condtion.notify()
    return value

def main():
    lock = threading.Lock()
    condition = threading.Condition(lock)
    threads = []
    condition.acquire()
    for i in range(10):
        thread_id = threading.Thread(target=worker,args=(lock,i,randint(0,5),condition))
        thread_id.start()
        threads.append(thread_id)
    print("Main: Waiting for condition")
    condition.wait()
    for j in range(10):
        threads[j].join()
    print("Done")

if __name__ == "__main__":
    main()

