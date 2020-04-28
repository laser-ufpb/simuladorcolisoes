from drone import Drone
import numpy as np
from random import randint
from random import uniform

class Circle(Drone):
    def __init__(self, num_steps):
        super().__init__(num_steps) 

    def movCircle(self):
        """ theta = np.linspace(-4 * np.pi, 4 * np.pi, 10)
        z = np.linspace(10, 10, 10) movimento estrelar"""
        par = randint(1,4)
        theta = np.linspace((-1*par) * np.pi, par * np.pi, self)

        z = np.linspace(randint(0,4), randint(0,4), self)
        r = z**2 + 1

        x = r * np.sin(theta)
        y = r * np.cos(theta)
        print(r)
        return x, y, z

    def movCircle2(self,theta,z,i):
        """ theta = np.linspace(-4 * np.pi, 4 * np.pi, 10)
        z = np.linspace(10, 10, 10) movimento estrelar"""
        '''
        par = randint(1, 4)
        theta = np.linspace((-1*par) * np.pi, par * np.pi, self)
        '''
        
        r = z[i]**2 + 1
        
        x = r * np.sin(theta[i])
        y = r * np.cos(theta[i])

        """ print(x)
        print(y)
        print(z[i]) """
         
        return x, y, z[i]
