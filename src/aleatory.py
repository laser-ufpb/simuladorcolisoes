from drone import Drone
from random import uniform
import numpy as np
from random import randint


class Aleatory(Drone):
    def __init__(self, num_steps):
        super().__init__(num_steps)
    
    def mov(self, x_1, y_1, z_1):
              
        dro = Drone(self)

        sets = 10
        zaux = []
        xaux = []
        yaux = []

        '''
        for i in range(self):
            dro.x[i] = uniform(0.0, (x_1))
            dro.y[i] = uniform(0.0, (y_1))
            dro.z[i] = uniform(0.0, (z_1))
        '''    
        partes = self/sets
        for j in range(sets):

            par = randint(1, 4)
            theta = np.linspace((-1*par) * np.pi, par * np.pi, partes)
            z = uniform(np.linspace(randint(0, 2),
                                    randint(0, 2), partes), randint(-1, int(z_1)))
            r = (z**2 + 1)*x_1*y_1*z_1
            x = uniform(r * np.sin(theta), randint(-1, int(x_1)))
            y = uniform(r * np.cos(theta), randint(-1, int(y_1)))
            
            """ print("X[",j,"]:",x)
            print("Y[",j,"]:",y)
            print("Z[",j,"]:",z) """

            for i in range(int(partes)):
                xaux.append(x[i])
                yaux.append(y[i])
                zaux.append(z[i])

            
            """ for i in range(int(partes)):
                dro.x[j*i] = x[i] #* randint(100,120)/100
                dro.y[j*i] = y[i] * randint(100, 120)/100
                dro.z[j*i] = z[i]  # * randint(100, 120)/100 """
            
        

        dro.x = xaux
        dro.y = yaux
        dro.z = zaux
        
            #x_1, y_1, z_1 = dro.x[i], dro.y[i], dro.z[i]
  
        return dro.x, dro.y, dro.z


    def movCircle(self):
        """ theta = np.linspace(-4 * np.pi, 4 * np.pi, 10)
        z = np.linspace(10, 10, 10) movimento estrelar"""
        par = randint(1, 4)
        theta = np.linspace((-1*par) * np.pi, par * np.pi, self)
        z = np.linspace(randint(0, 4), randint(0, 4), self)
        r = z**2 + 1
        x = r * np.sin(theta)
        y = r * np.cos(theta)

    
