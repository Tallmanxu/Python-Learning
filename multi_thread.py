import threading  
import time
import thread

class timer(threading.Thread): #The timer class is derived from the class threading.Thread  
    def __init__(self, num, interval):  
        threading.Thread.__init__(self)  
        self.thread_num = num  
        self.interval = interval  
        self.thread_stop = False  
   
    def run(self): #Overwrite run() method, put what you want the thread do here  
        while not self.thread_stop:  
            print 'Thread Object(%d), Time:%s\n' %(self.thread_num, time.ctime())  
            time.sleep(self.interval)  
    def stop(self):  
        self.thread_stop = True  
         
   
def test1():
    thread1 = timer(1, 1)  
    thread2 = timer(2, 2)
    thread3 = timer(3, 3)
    thread1.start()  
    thread2.start()  
    time.sleep(5)
    thread3.start()
    time.sleep(5)
    thread1.stop()  
    thread2.stop()
    thread3.stop()
    return  





mylock = threading.RLock()
num=0

class myThread(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self)
        self.t_name = name

    def run(self):
        global num
        while True:
            mylock.acquire()

            print '\nThread(%s) locked, Number: %d'%(self.t_name, num)
            if num>=4:
                mylock.release()
                print '\nThread(%s) released, Number: %d'%(self.t_name, num)
                break
            num+=1
            print '\nThread(%s) released, Number: %d'%(self.t_name, num)
            mylock.release()

def test2():
    '''this is func1'''
    '''hi'''
    thread1 = myThread('A')
    thread2 = myThread('B')
    '''I just have a test.test over
   '''
    thread1.start()
    thread2.start()
    '''''I just have a test.

   2       test over'''




#test2()
print test2.__doc__