# from random import choice
# end_wins=0
# end_lose=0
# for games in range(10000):
#     airplane={}
#     apass=list(range(100))
#     sits=list(range(100))
#     fp=choice(apass)
#     fs=choice(sits)
#     airplane[fp]=fs
#     apass.remove(fp)
#     sits.remove(fs)
#     np=len(apass)
#     for i in range(np):
#         rp=choice(apass)
#         if rp in sits:
#             rs=rp
#             airplane[rp]=rs
#         else:
#             rs=choice(sits)
#             airplane[rp]=rs
#         apass.remove(rp)
#         sits.remove(rs)
#         if i==np-1:
#             if airplane[rp]==rp:
#                 end_wins+=1
#             else:
#                 end_lose+=1
# print(end_wins/10000)
import matplotlib.pyplot as plt
import numpy
manx=[]
many=[]
for cx in numpy.arange(-2,2.01, 0.01):
    for cy in numpy.arange(-2,2.01, 0.01):
        x=0
        y=0
        a=0
        n=0
        while a<10 and n<=20:
            xn1 = x**2 - y**2 + cx
            yn1 = 2*x*y + cy
            a = (x**2+y**2)**0.5
            x=xn1
            y=yn1
            n+=1
        if n >=20:
            manx.append(cx)
            many.append(cy)
plt.scatter(manx, many, marker='.', s=6)
plt.show()

