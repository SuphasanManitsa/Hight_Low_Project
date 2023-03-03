from Hight_Low import Hight_Low
hl = Hight_Low()
import numpy as np
import matplotlib.pyplot as plt
balance = 100

#-----------------------------------  teng
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง ในแต่ละเลขที่เลือกเต็ง พบว่า อัตราการการนะอยู่ที่ราวๆ 42% 
# plt.figure(figsize = (12,12))
# for j in range(9):
#     x = []
#     y = []
#     for i in range(1,7):
#         values = hl.teng(balance = balance,hit = 1,n = 10000000,re = 1,a = i)
#         x.append(i)
#         y.append(values)
#     plt.subplot(3,3,j+1)
#     plt.plot(x,y)
#     plt.title(f'i={j + 1}')
# plt.show()
#-----------------------------------  tode
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง ในแต่ละเลขที่เลือกโต๊ด พบว่า อัตราการการนะอยู่ที่ราวๆ 14% 
# tod = []
# for i in range(1,7):
#     tod.append([])
#     for j in range(1,7):
#         if i == j:
#             continue
#         tod[i - 1].append([i,j])
        
# plt.figure(figsize = (18,12))
# count = 1
# for i in tod:
#     plt.subplot(2,3,count)
#     count += 1
#     for j in i:
#         y = hl.tode(balance = balance,hit = 1,n = 10000000,re = 1,a = j)
#         plt.xlim(0,7)
#         plt.plot(j[1],y,"o")
#         plt.title(f'Tod {count - 1}')
# plt.show()
#-----------------------------------  hight_low
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่นสูงอยู่ที่ราวๆ 50% และ อัตราการชนะของการเล่นต่ำอยู่ที่ราวๆ 37.5%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     plt.subplot(3,3,i + 1)
#     x_one = np.ones(100)
#     x_zero = np.zeros(100)
#     o = []
#     z = []
#     for j,k in zip(x_one,x_zero):
#         o.append(hl.hight_low(balance = balance,hit = 1,n = 10000,re = 1,a = j))
#         z.append(hl.hight_low(balance = balance,hit = 1,n = 10000,re = 1,a = k))
#     plt.plot(x_one,o)
#     plt.plot(x_zero,z)
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่น 11 อยู่ที่ราวๆ 12.5%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     x_one = np.ones(100)
#     o = []
#     for _ in range(100):
#         o.append(hl.mid_hight_low(balance = balance,hit = 1,n = 1000000,re = 1))
#     plt.subplot(3,3,i+1)
#     plt.plot(x_one,o)
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่น ตองของแต่ละเลข อยู่ที่ราวๆ 0.46%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     plt.subplot(3,3,i+1)
#     a = []
#     for j in range(6):
#         a.append(hl.tong(balance = balance,hit = 1,n = 10000000,re = 1,a = j + 1))
#         plt.xlim(0,7)
#     plt.plot(range(1,7),a,"o")
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# plt.figure(figsize = (12,12))
# for i in range(3):
#     plt.subplot(2,3,i+1)
#     a = []
#     for j in range(1,7):
#         a.append(hl.hight_low_whit_args(balance = balance,hit = 1,n = 100000,re = 1,a = [0,j]))
#     plt.xlim(0,7)
#     plt.plot(range(1,7),a)
#     plt.title(f'low {i + 1}')
    
# for i in range(3,6):
#     plt.subplot(2,3,i+1)
#     a = []
#     for j in range(1,7):
#         a.append(hl.hight_low_whit_args(balance = balance,hit = 1,n = 100000,re = 1,a = [1,j]))
#     plt.xlim(0,7)
#     plt.plot(range(1,7),a)
#     plt.title(f'hight {i - 2}')
# plt.show()
#-----------------------------------













# def f(balance,day,hit):
#     a = []
#     for i in range(day):
#         if balance <= 0:
#             print(balance)
#             break
#         # print(f"day {i + 1}")
#         balance_day = balance
#         stop_loss = balance - balance * 0.0001
#         stop_win = balance + balance * 0.0002
        
#         while True:
#             # print(f"time {j +  1}")
#             if balance <= stop_loss or balance >= stop_win:
#                 break
#             balance_cp = balance
#             balance = hl.teng(balance = balance,hit = hit,n = 1,re = 0,a = 1)

#             if balance < balance_cp:
#                 # print("loss")
#                 hit *= 2
#             else:
#                 # print("win")
#                 hit = balance_day * 0.000001
#         a.append(balance)
#     # print("-------")
#     return a

# import numpy as np
# import matplotlib.pyplot as plt
# balance = 1000000
# hit = balance * 0.000001
# day = 1 * 30 * 12
# yy = np.array(f(balance=balance,day=day,hit=hit))
# xx = np.linspace(1,len(yy),len(yy))
# print(len(xx))
# print(len(yy))
# plt.plot(xx,yy)
# plt.show()