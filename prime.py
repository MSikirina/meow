pr=[]
for i in range(100):
    for j in range(i//2):
        if j!=0 and i%j==0 and j!=1:
            print('составное число', i)
            break
        else:
            pr.append(i)
print(pr)
            