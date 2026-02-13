import random
import matplotlib.pyplot as plt
lgood=0
for L in range(1000):
    N=0
    op=[]
    for N in range(100):
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
        if lseq==10:
            seq6+=1
    if seq6>0:
        lgood+=1
print(lgood/1000)
    #     if a==1:
    #         op.append(1)
    #         N+=1
    #     else:
    #         op.append(0)
    #         N+=1
    # print(op)
