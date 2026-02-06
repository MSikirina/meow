import matplotlib.pyplot as plt

class Alien:
    Al_count=0

    def __init__(self, x, y, h=5):
        self.x=x
        self.y=y
        self.h=h
        Alien.Al_count+=1

    def tp(self):
        pass

al=Alien(10,10)
al2 = Alien(0,0)
print(al.x,al.y)
print(Alien.Al_count)
