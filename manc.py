import numpy as np
import matplotlib.pyplot as plt
def c_cmat(xmin, xmax, ymin, ymax, den):
    re=np.linspace(xmin, xmax, int((xmax-xmin)*den))
    im=np.linspace(ymin, ymax, int((ymax-ymin)*den))
    mat=re[np.newaxis,:]+im[:,np.newaxis]*1j
    return mat
print(c_cmat(-2,2.1,-2,2,10))
