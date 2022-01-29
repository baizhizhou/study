
# 利用函数创建多线程
import threading
import time

'''
def main(name='python'):
    for i in range(2):
        print('hellow',name)
        time.sleep(1)
# 创建线程1,不指定参数
thread_01 = threading.Thread(target=main)
# 启动线程1
thread_01.start()
# 创建线程2，指定参数
thread_02 = threading.Thread(target=main,args=('wwww',))
# 启动线程2
thread_02.start()'''

# 利用类函数创建多线程
'''
    我们要自定义一个类，对于这个类有两点要求，
    必须继承 threading.Thread 这个父类；
    必须覆写 run 方法。
'''
from threading import Thread
class mythread(Thread):
    def __init__(self,name = 'python'):
        super().__init__() # 继承父类的init方法,一定要写在最前面
        self.name = name
    def run(self):
        for i in range(2):
            print('hellow', self.name)
            time.sleep(1)
thread_01 = mythread()
thread_01.start()

# 创建线程02，指定参数
thread_02 = mythread("MING")
thread_02.start()

