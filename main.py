# from random import uniform
# N=10000
# NS=0
# for i in range(N):
#     x=uniform(0,1)
#     y=uniform(0,1)
#     if x**2+y**2<=1:
#         NS+=1
# print(NS/N*4)

# def mycyph(text,key):
#     alpha="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
#     alph=list(alpha)
#     s=''
#     for b in list(text):
#         if b in alph:
#             n=alph.index(b)
#             nn=n+key
#             if nn<=32:
#                 d=alph[nn]
#             else:
#                 d=alph[nn%33]
#         else:
#             d=b
#         s=s+d
#     return s
# text=input("введите слово ")
# c=int(input("введите ключ "))
# ct=mycyph(text,c)
# print(ct)
# ut=mycyph(ct,-c)
# print(ut)

f=open('alice.txt',encoding='utf-8')
lines=f.read()
d={}
a=0
alpha=list("абвгдеёжзийклмнопрстуфхцчшщъыьэюя")
for ch in lines:
    ch=ch.lower()
    if ch in alpha:
        if d.get(ch,0)==0:
            d[ch]=1
        else:
            d[ch]+=1
        a+=1
f.close()
sum=0
for k in d:
    sum+=d[k]
    n=d[k]/a
    d[k]=n
    print(k,'=',n)
print(a,sum)
maxn=0
maxa=''
for k in d:
    if d[k]>maxn:
        maxn=d[k]
        maxa=k
print(maxa,maxn)

