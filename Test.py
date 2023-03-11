from Hight_Low import Hight_Low
import matplotlib.pyplot as plt
hl = Hight_Low()
balance = 100
plt.figure(figsize = (12,12))
for i in range(3):
    plt.subplot(2,3,i+1)
    a = []
    for j in range(1,7):
        a.append(hl.hight_low_whit_args(balance = balance,hit = 1,n = 100000,re = 1,a = [0,j],gong = [0,0]))
    plt.xlim(0,7)
    plt.plot(range(1,7),a)
    plt.title(f'low {i + 1}')
plt.show()