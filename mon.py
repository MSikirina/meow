# import random
# import matplotlib.pyplot as plt
# lgood=0
# M=8
# Nmax=100
# for L in range(1000):
#     N=0
#     op=[]
#     for N in range(100):
#         a=random.choice([1,0])
#         op.append(a)
#     c=op[0]
#     lseq=0
#     seq6=0
#     for res in op:
#         if res==c:
#             lseq+=1
#         else:
#             res=c
#             lseq=1
#         if lseq==8:
#             seq6+=1
#     if seq6>0:
#         lgood+=1
# print(lgood/1000)
# print(N)
# print(L)
c=0
num=input('введите номер карты ')
a=list(num)
for index,element in enumerate(a):
    print(index, element)
    element=int(element)
    if index%2==0:
        element=element*2
        if element>9:
            element-=9
    c+=element
print(c)


