from Hight_Low import Hight_Low
hl = Hight_Low()
balance = 100
print(hl.teng(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(hl.tode(balance = balance,hit = 1,n = 1000000,re = 1,a = [1,2]))
print(hl.hight_low(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(hl.mid_hight_low(balance = balance,hit = 1,n = 1000000,re = 1))
print(hl.tong(balance = balance,hit = 1,n = 1000000,re = 1,a = 1))
print(hl.hight_low_whit_args(balance = balance,hit = 1,n = 1000000,re = 1,a = [1,1]))