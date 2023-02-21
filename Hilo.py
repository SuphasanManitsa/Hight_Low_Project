import matplotlib.pyplot as plt
import numpy as np

def cartesian_product(*arrays):
    la = len(arrays)
    dtype = np.result_type(*arrays)
    arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
    for i, a in enumerate(np.ix_(*arrays)):
        arr[..., i] = a
    return arr.reshape(-1, la)

def mon_sim(n):
    # c == 1 แทงเต็ง คือ แทงแต้ม 1-6 ถ้าทายถูกอย่างน้อย 1 ใน 3 จะได้เงิน 1 ต่อ 1
    # c == 2 แทงโต๊ด คือ แทงทีละ 2 แต้ม ลูกเต๋า 2 ใน 3 ถ้าทายถูกอย่างน้อย 2 ใน 3 จะได้เงิน 5 ต่อ 1
    # c == 3 แทงสูงต่ำ คือ 3-10 == ต่ำ : 12-18 == สูง จะได้เงิน 1 ต่อ 1
    # c == 4 แทง 11 ไฮโล คือ ถ้าผลรวมของลูกเต๋าทั้ง 3 ลูก == 11 จะได้เงิน 5 ต่อ 1
    A = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
    B = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
    C = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
    sum = A + B + C
    return A,B,C,sum

def teng(balance,hit,n,re : bool,a):
    '''
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(np.logical_or(np.logical_or(A == a, B == a), C == a), 1, 0)
    cost = np.sum(np.where(vA == 1, hit,hit * (-1)))
    static_win = np.sum(np.where(vA == 1, 1, 0))
    static_loss = np.sum(np.where(vA == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n
    
def tode(balance,hit,n,re : bool,a = []):
    '''
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(np.logical_or(np.logical_or(A == a[0], B == a[0]), C == a[0]), 1, 0)
    vB = np.where(np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1]), 1, 0)
    vAB = vA * vB
    cost = np.sum(np.where(vAB == 1, hit * 5,hit * (-1)))
    static_win = np.sum(vAB)
    static_loss = np.sum(np.where(vAB == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n
    
def hight_low(balance,hit,n,re : bool,a):
    '''
    a == 1 == hight
    a == 0 == low
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(np.logical_and(sum < 11, a == 0), 1, 0)
    vB = np.where(np.logical_and(sum > 11, a == 1), 1, 0)
    vAB = vA + vB
    cost = np.sum(np.where(vAB == 1, hit, (-1) * hit))
    static_win = np.sum(vAB)
    static_loss = np.sum(np.where(vAB == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n
    
def mid_hight_low(balance,hit,n,re : bool):
    '''
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(sum == 11, 1, 0)
    cost = np.sum(np.where(vA == 1, hit * 5,hit * (-1)))
    static_win = np.sum(vA)
    static_loss = np.sum(np.where(vA == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n

def tong(balance,hit,n,re : bool,a):
    '''
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(np.logical_and(np.logical_and(A == a, B == a), C == a), 1, 0)
    cost = np.sum(np.where(vA == 1, hit * 5,hit * (-1)))
    static_win = np.sum(vA)
    static_loss = np.sum(np.where(vA == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n

def hight_low_whit_args(balance,hit,n,re : bool,a = []):
    '''
    a[0] == 1 == hight
    a[0] == 0 == low
    a[1] == 1 - 6
    re == 0 : return balance
    re == 1 : return static win
    '''
    A,B,C,sum = mon_sim(n)
    vA = np.where(np.logical_and(np.logical_and(a[0] == 1,sum > 11),np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1])), 1, 0)
    vB = np.where(np.logical_and(np.logical_and(a[0] == 0,sum < 11),np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1])), 1, 0)
    vAB = vA + vB
    cost = np.sum(np.where(vAB == 1, hit * 2,hit * (-1)))
    static_win = np.sum(vAB)
    static_loss = np.sum(np.where(vAB == 0, 1, 0))
    if re == 0:
        return balance + cost
    else:
        return static_win / n
# mon_sim = np.vectorize(mon_sim)
balance = 100
#print(mid_hight_low(balance = balance,hit = 1,n = 1000000,re = 1))
print(teng(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(tode(balance = balance,hit = 1,n = 1000000,re = 1,a = [1,2]))
print(hight_low(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(mid_hight_low(balance = balance,hit = 1,n = 1000000,re = 1))
print(tong(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(hight_low_whit_args(balance = balance,hit = 1,n = 1000000,re = 1,a = [1,1]))
# ----------------------------------- Test c == 1
# plt.figure(figsize=(12, 12))
# x = np.linspace(1,6,6)
# for i in range(9):
#     # สามารถกำหนดตำแหน่ง subplot
#     plt.subplot(3, 3, i+1)
#     a = []
#     for j in range(1,7):
#         a.append(mon_sim(balance, 1, 1000000, 1, [j]))
#     plt.plot(x,a,"o")
#     plt.title(f'i={i}')
# plt.show()
# ----------------------------------- Test c == 1
# ----------------------------------- Test c == 2
# tode = cartesian_product(np.arange(1, 7), np.arange(1, 7))
# for i in range(6):
#     tode = np.delete(tode, 6 * i, 0)
# x = np.linspace(1, 30, 30)
# plt.figure(figsize=(12, 12))
# for i in range(9):
#     # สามารถกำหนดตำแหน่ง subplot
#     plt.subplot(3, 3, i+1)
#     a = []
#     for j in tode:
#         a.append(mon_sim(balance, 1, 1000000, 2, j))
#     plt.plot(x, a, "o")
#     plt.title(f'i={i}')
# plt.show()
# ----------------------------------- Test c == 2
# ----------------------------------- Test c == 3
# plt.figure(figsize=(12, 12))
# x = np.linspace(1, 100, 100)
# xx = [np.linspace(0, 0, 100), np.linspace(1, 1, 100)]
# for i in range(2):
#     plt.subplot(1, 2, i + 1)
#     a = []
#     y = np.array(
#         list(map(lambda x: mon_sim(balance, 1, 1000000, 3, [x]), xx[i])))
#     plt.plot(x, y, "o")
#     plt.title(f'i={i}')
# plt.show()
# ----------------------------------- Test c == 3
# ----------------------------------- Test c == 4
# x = np.linspace(1, 100, 100)
# y = np.array(list(map(lambda x: mon_sim(balance, 1, 1000000, 4,), x)))
# #y = np.array(mon_sim(balance, 1, 1000000, 4, x))
# print(x)
# print(y)
# plt.plot(x,y,"o")
# plt.show()
# ----------------------------------- Test c == 4
