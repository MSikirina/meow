from random import choice
end_wins=0
end_lose=0
for games in range(10000):
    airplane={}
    apass=list(range(100))
    sits=list(range(100))
    fp=choice(apass)
    fs=choice(sits)
    airplane[fp]=fs
    apass.remove(fp)
    sits.remove(fs)
    np=len(apass)
    for i in range(np):
        rp=choice(apass)
        if rp in sits:
            rs=rp
            airplane[rp]=rs
        else:
            rs=choice(sits)
            airplane[rp]=rs
        apass.remove(rp)
        sits.remove(rs)
        if i==np-1:
            if airplane[rp]==rp:
                end_wins+=1
            else:
                end_lose+=1
print(end_wins/10000)

