import matplotlib.pyplot as plt
import numpy as np

class Hight_Low:
    def cartesian_product(self,*arrays):
        la = len(arrays)
        dtype = np.result_type(*arrays)
        arr = np.empty([len(a) for a in arrays] + [la], dtype=dtype)
        for i, a in enumerate(np.ix_(*arrays)):
            arr[..., i] = a
        return arr.reshape(-1, la)

    def mon_sim(self,n):
        A = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
        B = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
        C = np.random.choice(a=[1, 2, 3, 4, 5, 6], size=n, replace=True)
        sum = A + B + C
        return A,B,C,sum

    def teng(self,balance,hit,n,re : bool,a,gong = []):
        '''
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(np.logical_or(np.logical_or(A == a, B == a), C == a), 1, 0)
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vA = np.where(vA == 1, 1,np.where(b <= gong[1],1,0))
            
        cost = np.sum(np.where(vA == 1, hit,hit * (-1)))
        static_win = np.sum(np.where(vA == 1, 1, 0))
        static_loss = np.sum(np.where(vA == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n
        
    def tode(self,balance,hit,n,re : bool,a = [],gong = []):
        '''
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(np.logical_or(np.logical_or(A == a[0], B == a[0]), C == a[0]), 1, 0)
        vB = np.where(np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1]), 1, 0)
        vAB = vA * vB
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vAB = np.where(vAB == 1, 1,np.where(b <= gong[1],1,0))
            
        cost = np.sum(np.where(vAB == 1, hit * 5,hit * (-1)))
        static_win = np.sum(vAB)
        static_loss = np.sum(np.where(vAB == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n
        
    def hight_low(self,balance,hit,n,re : bool,a,gong = []):
        '''
        a == 1 == hight
        a == 0 == low
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(np.logical_and(sum < 11, a == 0), 1, 0)
        vB = np.where(np.logical_and(sum > 11, a == 1), 1, 0)
        vAB = vA + vB
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vAB = np.where(vAB == 1, 1,np.where(b <= gong[1],1,0))
            
        cost = np.sum(np.where(vAB == 1, hit, (-1) * hit))
        static_win = np.sum(vAB)
        static_loss = np.sum(np.where(vAB == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n
        
    def mid_hight_low(self,balance,hit,n,re : bool,gong = []):
        '''
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(sum == 11, 1, 0)
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vA = np.where(vA == 1, 1,np.where(b <= gong[1],1,0))
            
        cost = np.sum(np.where(vA == 1, hit * 5,hit * (-1)))
        static_win = np.sum(vA)
        static_loss = np.sum(np.where(vA == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n

    def tong(self,balance,hit,n,re : bool,a,gong = []):
        '''
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(np.logical_and(np.logical_and(A == a, B == a), C == a), 1, 0)
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vA = np.where(vA == 1, 1,np.where(b <= gong[1],1,0))
        
        cost = np.sum(np.where(vA == 1, hit * 5,hit * (-1)))
        static_win = np.sum(vA)
        static_loss = np.sum(np.where(vA == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n

    def hight_low_whit_number(self,balance,hit,n,re : bool,a = [],gong = []):
        '''
        a[0] == 1 == hight
        a[0] == 0 == low
        a[1] == 1 - 6
        re == 0 : return balance
        re == 1 : return static win
        
        gong[0] == 1 : gong
        gong[0] == 0 : no gong
        gong[1] == 0 : persen gong
        '''
        A,B,C,sum = self.mon_sim(n)
        vA = np.where(np.logical_and(np.logical_and(a[0] == 1,sum > 11),np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1])), 1, 0)
        vB = np.where(np.logical_and(np.logical_and(a[0] == 0,sum < 11),np.logical_or(np.logical_or(A == a[1], B == a[1]), C == a[1])), 1, 0)
        vAB = vA + vB
        
        if gong[0] == 1:
            b = np.random.uniform(0,1,n)
            vAB = np.where(vAB == 1, 1,np.where(b <= gong[1],1,0))
            
        cost = np.sum(np.where(vAB == 1, hit * 2,hit * (-1)))
        static_win = np.sum(vAB)
        static_loss = np.sum(np.where(vAB == 0, 1, 0))
        if re == 0:
            return balance + cost
        else:
            return static_win / n

    def f1(self,balance,day,hit,gong = []):
        a = []
        for i in range(day):
            if balance <= 0:
                print(balance)
                break
            balance_day = balance
            stop_loss = balance - balance * 0.0002
            stop_win = balance + balance * 0.0003
            
            while True:
                if balance <= stop_loss or balance >= stop_win:
                    break
                balance_cp = balance
                balance = self.hight_low(balance = balance,hit = hit,n = 1,re = 0,a = 0,gong = gong)

                if balance < balance_cp:
                    hit *= 2
                else:
                    hit = balance_day * 0.000001
            a.append(balance)
        return a

    def f2(self,balance,day,hit,gong = []):
        a = []
        for i in range(day):
            if balance <= 0:
                print(balance)
                break
            balance_day = balance
            stop_loss = balance - balance * 0.0001
            stop_win = balance + balance * 0.0002
            
            while True:
                if balance <= stop_loss or balance >= stop_win:
                    break
                balance_cp = balance
                balance = self.hight_low(balance = balance,hit = hit,n = 1,re = 0,a = 0,gong = gong)

                if balance > balance_cp:
                    hit *= 2
                else:
                    hit = balance_day * 0.000001
            a.append(balance)
        return a
    
    def pud_sed(self,a):
        a,b = str(a).split(".")
        b = (b + "00")[:3]
        a += b[:2]
        a = list(a[::-1])
        b = int(b[2])
        if b >= 5:
            for i in range(len(a)):
                if i == len(a) - 1 and a[i] == "9":
                    a[i] = "0"
                    a += ["1"]
                    break
                if a[i] == "9":
                    a[i] = "0"
                else:
                    a[i] = str(int(a[i]) + 1)
                    break
        a.insert(2,".")
        a = "".join(a)[::-1]
        return float(a)