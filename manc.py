import numpy as np
import matplotlib.pyplot as plt
def c_cmat(xmin, xmax, ymin, ymax, den):
    re=np.linspace(xmin, xmax, int((xmax-xmin)*den))
    im=np.linspace(ymin, ymax, int((ymax-ymin)*den))
    mat=re[np.newaxis,:]+im[:,np.newaxis]*1j
    return mat
#print(c_cmat)

def stable(mat, n):
    z=0
    for i in range(n):
        z=z**2+mat
    return abs(z)<=2

def ju( n, c):
    z=c_mat(-2, 0.5, -1.5, 1.5, 2000)
    for i in range(n):
        z=z**2+c
    return abs(z)<=2
c=c_cmat(-2, 0.5, -1.5, 1.5, 2000)
man=stable(c, 35)
plt.imshow(man, cmap='jet')
plt.gca().set_aspect('equal')
plt.show()
juju=ju(20, 0.5)

plt.imshow(ju, cmap='jet')
plt.gca().set_aspect('equal')
plt.show()