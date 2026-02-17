import random
import matplotlib.pyplot as plt
def Coin(N, M, L):
    lgood=0
    for j in range(L):
        op=[]
        for i in range(N):
            a=random.choice([1,0])
            op.append(a)
        c=op[0]
        lseq=0
        seq6=0
        for res in op:
            if res==c:
                lseq+=1
            else:
                res=c
                lseq=1
            if lseq==M:
                seq6+=1
        if seq6>0:
            lgood+=1
    return lgood/L
x=[]
y=[]
for u in range(2, 10):
    x.append(u)
    y.append(Coin(100, u, 1000))
    print(u, Coin(100, u, 1000))
plt.scatter(x, y)
plt.show()