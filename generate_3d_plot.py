import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def u(t, k, n): # An arbitrary utility function
    U = np.zeros((n, n))
    for i, ti in enumerate(t):
        for j, ki in enumerate(k):
            if ti < ki:
                U[i][j] = 1 / (ti + ki / 10 + 1) ** .5
            else:
                U[i][j] = 0
    return U


if __name__ == "__main__":    

    n = 30
    mainsize = 15

    x = np.linspace(0, 30, n)
    y = np.linspace(0, 30, n)

    X, Y = np.meshgrid(x, y)
    
    Z = u(y, x, n)

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    # ax.set_box_aspect((np.ptp(Y), np.ptp(X), 10 * np.ptp(Z)))
    ax.plot_surface(Y, X, Z, rstride=1, cstride=1, cmap='plasma', edgecolor='none')

    ax.set_xticks([0, 5, 10, 15, 20, 25, 30])
    ax.set_yticks([0, 10, 20, 30])
    
    ax.set_xlim(0, 30)
    ax.set_ylim(0, 30)    
    ax.set_zlim(0, 1)
    ax.view_init(elev=10, azim=260)

    ax.set_xlabel(r"$t$", fontsize=mainsize)
    ax.set_ylabel(r"$\kappa$", fontsize=mainsize)

    plt.savefig('img/3dplot1.pdf', bbox_inches='tight')
    # plt.clf()

    ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
    ax.view_init(elev=10, azim=330)
    plt.savefig('img/3dplot2.pdf', bbox_inches='tight')


