from drone import Drone

class Chaotic (Drone):
    def __init__(self, num_steps):
        super().__init__(num_steps)
    def lorenz(self, x_1, y_1, z_1):
        s=10
        r=28
        b=2.667
        '''
        Given:
        x, y, z: a point of interest in three dimensional space
        s, r, b: parameters defining the lorenz attractor
        Returns:
        x_dot, y_dot, z_dot: values of the lorenz attractor's partial
            derivatives at the point x, y, z
        '''
        dt = 0.01
        
        dro = Drone(self)
        dro.x[0],dro.y[0],dro.z[0] = x_1,y_1,z_1 

        for i in range(self):
            x_dot = s*(y_1 - x_1)
            y_dot = r*x_1 - y_1 - x_1*z_1
            z_dot = x_1*y_1 - b*z_1

            """ traj = Chaotic(num_steps)
            x_dot, y_dot, z_dot = traj.lorenz(dro.x[i], dro.y[i], dro.z[i]) """

            dro.x[i + 1] = dro.x[i] + (x_dot * dt)
            dro.y[i + 1] = dro.y[i] + (y_dot * dt)
            dro.z[i + 1] = dro.z[i] + (z_dot * dt)

            x_1, y_1, z_1 = dro.x[i + 1], dro.y[i + 1], dro.z[i + 1]
        #print(dro.x,dro.y,dro.z)
        return dro.x, dro.y, dro.z

    def lorenz2(self, x_1, y_1, z_1):

        s=10
        r=28
        b=2.667
        '''
        Given:
        x, y, z: a point of interest in three dimensional space
        s, r, b: parameters defining the lorenz attractor
        Returns:
        x_dot, y_dot, z_dot: values of the lorenz attractor's partial
            derivatives at the point x, y, z
        '''
        dt = 0.01
        
        
        x_dot = s*(y_1 - x_1)
        y_dot = r*x_1 - y_1 - x_1*z_1
        z_dot = x_1*y_1 - b*z_1

      

        prox_x = x_1 + (x_dot * dt)
        prox_y = y_1 + (y_dot * dt)
        prox_z = z_1 + (z_dot * dt)

        
        #print(dro.x,dro.y,dro.z)
        return prox_x,prox_y,prox_z 