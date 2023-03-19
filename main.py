from Hight_Low import Hight_Low
hl = Hight_Low()
import numpy as np
import matplotlib.pyplot as plt
balance = 100

#-----------------------------------  teng
# จากข้อสรูป จากกว่ารันเทส 10 ล้านครั้ง ในแต่ละเลขที่เลือกเต็ง พบว่า อัตราการการนะอยู่ที่ราวๆ 42% 
# plt.figure(figsize = (12,12))
# for j in range(9):
#     x = []
#     y = []
#     for i in range(1,7):
#         values = hl.teng(balance = balance,hit = 1,n = 10000000,re = 1,a = i,gong = [0,0])
#         x.append(i)
#         y.append(values)
#     plt.subplot(3,3,j+1)
#     plt.plot(x,y)
#     plt.title(f'Test No. {j + 1}')
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
#         y = hl.tode(balance = balance,hit = 1,n = 10000000,re = 1,a = j,gong = [0,0])
#         plt.xlim(0,7)
#         plt.plot(j[1],y,"o")
#         plt.title(f'Tod {count - 1}')
# plt.show()
#-----------------------------------  hight_low
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่นต่ำอยู่ที่ราวๆ 50% และ อัตราการชนะของการเล่นาสูงอยู่ที่ราวๆ 37.5%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     plt.subplot(3,3,i + 1)
#     x_one = np.ones(10)
#     x_zero = np.zeros(10)
#     o = []
#     z = []
#     for j,k in zip(x_one,x_zero):
#         o.append(hl.hight_low(balance = balance,hit = 1,n = 10000000,re = 1,a = j,gong = [0,0]))
#         z.append(hl.hight_low(balance = balance,hit = 1,n = 10000000,re = 1,a = k,gong = [0,0]))
#     plt.plot(x_one,o)
#     plt.plot(x_zero,z)
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่น 11 อยู่ที่ราวๆ 12.5%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     x_one = np.linspace(1,100,100)
#     o = []
#     for _ in range(100):
#         o.append(hl.mid_hight_low(balance = balance,hit = 1,n = 1000000,re = 1,gong = [0,0]))
#     plt.subplot(3,3,i+1)
#     plt.plot(x_one,o)
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง 9 รอบ พบว่า อัตราการชนะของการเล่น ตองของแต่ละเลข อยู่ที่ราวๆ 0.0046%
# plt.figure(figsize = (12,12))
# for i in range(9):
#     plt.subplot(3,3,i+1)
#     a = []
#     for j in range(6):
#         a.append(hl.tong(balance = balance,hit = 1,n = 10000000,re = 1,a = j + 1,gong = [0,0]))
#         plt.xlim(0,7)
#     plt.plot(range(1,7),a,"o")
#     plt.title(f'Round {i + 1}')
# plt.show()
#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง ในแต่ละรอบ พบว่า
# สูง ต่ำ แบบเลือกเลขได้
# plt.figure(figsize = (12,12))
# for i in range(3):
#     plt.subplot(2,3,i+1)
#     a = []
#     for j in range(1,7):
#         a.append(hl.hight_low_whit_number(balance = balance,hit = 1,n = 10000000,re = 1,a = [0,j],gong = [0,0]))
#     plt.xlim(0,7)
#     plt.plot(range(1,7),a)
#     plt.title(f'low {i + 1}')
# print(a)
# for i in range(3,6):
#     plt.subplot(2,3,i+1)
#     a = []
#     for j in range(1,7):
#         a.append(hl.hight_low_whit_number(balance = balance,hit = 1,n = 10000000,re = 1,a = [1,j],gong = [0,0]))
#     plt.xlim(0,7)
#     plt.plot(range(1,7),a)
#     plt.title(f'hight {i - 2}')
# print(a)
# plt.show()
#-----------------------------------











#-----------------------------------
# จากข้อสรูป จากกว่ารับเทส 10 ล้านครั้ง ในแต่ละรอบ พบว่า 
# ถ้าเล่นตามกฎนี้
    # ถ้าเล่น n day โดยขนาดไม้ขึ้นอยู่กันจำนวนเงินคงเหลือ ในพอตโดยคิดเป็น %
    # แล้วมี stop win and stop loss ของแต่ละวัน
    # ในแต่ละวันให้เล่นไปเลื่อยๆจนถึง stop or stop win
    # ถ้ากรเล่นในรอบที่แล้วแพ้ก็เล่นไม้เท่าเดิม แต่ถ้าชนะ ไม้ต่อไปจะ คูณ 2 ไปเรื่อยๆจนกว่าจะแพ้ ถึงจะกลับมาเล่นขนาดไม้เท่าตอนแรก
    # ถ้าถึงแล้วให้จบการเล่นของวันนั้น
    # แล้ววันต่อมาให้คำนวนขนาดไม้ไหม่ และ stop win and stop loss ไหม่
# กราฟจะมีเทรนเป็นขาขึ้นแต่ก็มีโอกาศแพ้ได้ ถ้า stop loss ติดๆกันหลายวัน
# plt.figure(figsize = (12,12))
# balance = 1000000
# hit = balance * 0.000001
# day = 1 * 30 * 12
# for i in range(9):
#     plt.subplot(3,3,i+1)

#     yyy = np.array(hl.f1(balance=balance,day=day,hit=hit,gong = [0,0]))
#     xxx = np.linspace(1,len(yyy),len(yyy))
#     plt.plot(xxx,yyy)
    
#     yy = np.array(hl.f2(balance=balance,day=day,hit=hit,gong = [0,0]))
#     xx = np.linspace(1,len(yy),len(yy))
#     plt.plot(xx,yy)

#     y = np.array(hl.f3(balance=balance,day=day,hit=hit,gong = [0,0]))
#     x = np.linspace(1,len(yyy),len(yyy))
#     plt.plot(x,y)

#     plt.title(f'Round {i + 1}')
# plt.show()


#-----------------------------------
# balance = 1000
# balance = 1000
# for i in range(1,7):
#     teng = hl.teng(balance = balance,hit = 100,n = 10000000,re = 1,a = i,gong=[0,0])
#     print('Expectancy tang {0:d}: {1:.2f}'.format(i,(100 * teng)+(-100 * (1-teng))))

# tod = []
# for i in range(1,7):
#     tod.append([])
#     for j in range(1,7):
#         if i == j:
#             continue
#         tod[i - 1].append([i,j])
# for i in tod:
#     for j in range(5):
#         tode = hl.tode(balance = balance,hit = 100,n = 10000000,re = 1,a = i[j],gong=[0,0])
#         print('Expectancy tode {0:}: {1:.2f}'.format(i[j],(5*100 * tode)+(-100 * (1-tode))))

# high_low = hl.hight_low(balance = balance,hit = 100,n = 10000000,re = 1,a = 1,gong=[0,0])
# print('Expectancy high : {0:.2f}'.format((100 * high_low)+(-100 * (1-high_low))))

# high_low = hl.hight_low(balance = balance,hit = 100,n = 10000000,re = 1,a = 0,gong=[0,0])
# print('Expectancy low : {0:.2f}'.format((100 * high_low)+(-100 * (1-high_low))))

# mid_high_low = hl.mid_hight_low(balance = balance,hit = 100,n = 10000000,re = 1,gong=[0,0])
# print('Expectancy mid_high_low : {0:.2f}'.format((5*100 * mid_high_low)+(-100 * (1-mid_high_low))))

# for i in range(1,7):
#     tong = hl.tong(balance = balance,hit = 100,n = 10000000,re = 1,a = i,gong=[0,0])
#     print('Expectancy tong {0:d}: {1:.2f}'.format(i,(5*100 * tong)+(-100 * (1-tong))))

# for i in range(2):
#     for j in range(1,7):
#         high_low_whit_args = hl.hight_low_whit_number(balance = balance,hit = 100,n = 10000000,re = 1,a = [i,j],gong=[0,0])
#         print('Expectancy high_low_whit_args {0:d},{1:d}: {2:.2f}'.format(i,j,(2*100 * high_low_whit_args)+(-100 * (1-high_low_whit_args))))\

# def modetang(a,balance,h):
#     if a == 1:
#         return hl.teng(balance = balance,hit = h,n = 1,re = 0,a = np.random.randint(0,2),gong=[0,0])
#     elif a == 2:
#         return hl.tode(balance = balance,hit = h,n = 1,re = 0,a = [np.random.randint(0,7),np.random.randint(0,7)],gong=[0,0])
#     elif a == 3:
#         return hl.hight_low(balance = balance,hit = h,n = 1,re = 0,a = np.random.randint(0,2),gong=[0,0])
#     elif a == 4:
#         return hl.mid_hight_low(balance = balance,hit = h,n = 1,re = 0,gong=[0,0])
#     elif a == 5:
#         return hl.tong(balance = balance,hit = h,n = 1,re = 0,a = np.random.randint(0,7),gong=[0,0])
#     elif a == 6:
#         return hl.hight_low_whit_number(balance = balance,hit = h,n = 1,re = 0,a = [np.random.randint(0,2),np.random.randint(0,7)],gong=[0,0])

# def sung_tao(a,n):
#    X = []
#    Y = []
#    balance = 100000
#    h = 100
#    for i in range(n):
#        if balance <= 0:
#            balance
#        balance = modetang(a,balance,h)
#        h *= 2

#        X.append(i)
#        Y.append(balance)
#    plt.plot(X,Y)
#    plt.show()
#    return

# sung_tao(a = 3,n = 100)
#-----------------------------------
# n = 10000000
# #rate = np.linspace(0,1,n)
# x = np.linspace(0,n,n + 1)
# balance = 100
# a = []
# for i in x:
#     # balance_cp = balance
#     # balance = hl.hight_low(balance = balance,hit = 1,n = 1,re = 1,a = 0,gong = [0,i])
#     # if balance < balance_cp:
#     balance = hl.hight_low_whit_number(balance = balance,hit = 1,n = 1,re = 0,a = [0,1],gong=[0,0])
#     #balance =           hl.hight_low(balance = balance,hit = 1,n = 1,re = 0,a = 0,gong = [0,0])
#     a.append(balance)
# # p = np.poly1d(np.polyfit(x, a, 2))
# # plt.plot(x,p(x))
# plt.plot(x,a)

# # p = np.polyder(p, m=1)
# # for i in np.roots(p):
# #     print("%.5f" % i)
# #     print("%.5f" % p(i))
# #     print("--")

# plt.show()
#-----------------------------------

# n = 1000
# x = np.linspace(0,n,n)
# balance = 100
# a = []
# plt.figure(figsize = (20,12))
# w = 0
# l = 0
# for i in x:
#     ba = balance
#     balance = hl.hight_low(balance = balance,hit = 1,n = 1,re = 0,a = 0,gong=[0,0])
#     if ba > balance:
#         l += 1
#     elif ba < balance:
#         w += 1
#     a.append(balance)
# print(w,l)
# plt.plot(x,a)
# plt.show()

plt.figure(figsize = (20,12))
for j in range(9):
    x = []
    y = []
    for i in range(1,7):
        values = hl.teng(balance = balance,hit = 1,n = 10000000,re = 1,a = i,gong = [1,0.50])
        x.append(i)
        y.append(values)
    plt.subplot(3,3,j+1)
    plt.plot(x,y,"o")
    plt.title(f'Test No. {j + 1}')
plt.show()