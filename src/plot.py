import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Plot():
    def __init__(self,dro,qtde_drones):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        for i in range(qtde_drones):
            ax.plot(dro[i].x, dro[i].y, dro[i].z, lw=0.5)
        ax.set_xlabel("X Axis")
        ax.set_ylabel("Y Axis")
        ax.set_zlabel("Z Axis")
        ax.set_title("Simulação")
        plt.show()
