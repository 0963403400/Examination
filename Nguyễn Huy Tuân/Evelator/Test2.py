import numpy as np
import  time
import threading
class Evelator(threading.Thread):
    def __init__(self, floor, Number):
        threading.Thread.__init__(self)
        self.floor = floor
        self.Number = Number
        self.floorWaiting = []

    def ReceiveRequest(self,floor_Number):
        check=False
        if(self.floor!=floor_Number):
            for i in self.floorWaiting:
                if(i==floor_Number) : check=True
        else:
            print("This floor is here")
            return False;
        if(check==False):
            self.floorWaiting.append(floor_Number)
            return True
        else:
            return False

    def RunToFloor(self,floorNumber):
        while self.floor != floorNumber or self.floor != floorNumber:
            if self.floor > floorNumber:
                self.floor = self.floor-1
            else:
                self.floor = self.floor+1
            # time.sleep(2)
            print("Evelator "+ str(self.Number) + " is in floor "+ str(self.floor))
        # print("Evelator "+ str(self.Number) + " is in floor "+ str(floorNumber))

    def run(self):
        while(len(self.floorWaiting)!=0):
            time.sleep(1)
            self.RunToFloor(self.floorWaiting[0])
            self.floorWaiting.remove(self.floorWaiting[0])

# Tuan=Evelator(0,1)
#
# # Floor=input("What the floor do you want to go :")
# if(Tuan.ReceiveRequest(5)):print("Tang 5 da duoc dua vao hang doi")
# if(Tuan.ReceiveRequest(4)):print("Tang 4 da duoc dua vao hang doi")

# Tuan.start()









