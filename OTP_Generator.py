import time
from threading import Thread,Timer
import random
class OneTimePassword():
    def _init_(self):
        self.otp=0
        self.timer=0
        self.cotp=0
        self.t=0
        self.t2=None
        self.t1=None
    def generate(self):
        self.otp=random.randint(1000,9999)
        print(self.otp)
    def CountDown(self):
        self.t = 10
        self.t2=t2
        while(self.t>=0):
            if(self.t2.is_alive()):
                min,sec=divmod(self.t,60)
                f="{:02d}:{:02d}".format(min,sec)
                print(f,end="\r")
                self.t-=1
                time.sleep(1)
        return 0;
    def Input(self,arr,t1):
        self.cotp=int(input("Enter otp : "))
        self.t1=t1
        if(self.t1.is_alive()):
            if(self.cotp==self.otp):
                print("Accepted")
                return 0;
            else:
                print("Not Accepted")
                return 0;
        else:
            print("Invalid OTP")

        
arr=[]
obj=OneTimePassword()
t0=Thread(target=obj.generate)
t1=Thread(target=obj.CountDown,args=())
t2=Thread(target=obj.Input,args=(arr,t1))
t0.start()
t1.start()
t2.start()
