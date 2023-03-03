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
        # c == 1 แทงเต็ง คือ แทงแต้ม 1-6 ถ้าทายถูกอย่างน้อย 1 ใน 3 จะได้เงิน 1 ต่อ 1
        # c == 2 แทงโต๊ด คือ แทงทีละ 2 แต้ม ลูกเต๋า 2 ใน 3 ถ้าทายถูกอย่างน้อย 2 ใน 3 จะได้เงิน 5 ต่อ 1
        # c == 3 แทงสูงต่ำ คือ 3-10 == ต่ำ : 12-18 == สูง จะได้เงิน 1 ต่อ 1
        # c == 4 แทง 11 ไฮโล คือ ถ้าผลรวมของลูกเต๋าทั้ง 3 ลูก == 11 จะได้เงิน 5 ต่อ 1
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

    def hight_low_whit_args(self,balance,hit,n,re : bool,a = [],gong = []):
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
