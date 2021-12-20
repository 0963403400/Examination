from Test2 import Evelator
import time
import random
import threading
Floor_Number=10
Evelator_Number=4

# Khởi tạo 4 thang máy và 10 tầng
evelator1=Evelator(0,1)
evelator2=Evelator(0,2)
evelator3=Evelator(0,3)
evelator4=Evelator(0,4)

#Đưa 4 Request vào 4 thang máy
evelator1.ReceiveRequest(random.randint(1, 10))
evelator2.ReceiveRequest(random.randint(1, 10))
evelator3.ReceiveRequest(random.randint(1, 10))
evelator4.ReceiveRequest(random.randint(1, 10))

#Mỗi thang máy là một luồng chạy riêng, ta chạy 4 thang máy
evelator1.start()
evelator2.start()
evelator3.start()
evelator4.start()




