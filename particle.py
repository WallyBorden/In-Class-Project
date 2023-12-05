import matplotlib.pyplot as plt
import numpy as np

# dummy variables since they weren't defined in the OP
dz =1
Lz =2
Tw = 4
N = 30
Nt = 20
dt = 30

x = dz * np.random.random(N)
y = dz * np.random.random(N)
z = Lz * np.random.random(N)
vx = np.random.normal(0, Tw, N)
vy = np.random.normal(0, Tw, N)
vz = np.random.normal(0, Tw, N)

def particle(frame):
    """ Update function for animation """
    global x, y, z, scatter
        # Evolve
    for i in range(Nt):
        # Drift
        x += dt * vx
        y += dt * vy
        z += dt * vz
        
        # Collide specular wall (z=Lz)
        # Trace the straight-line trajectory to the top wall, bounce it back
        hit_top = z > Lz
        dt_ac = (z[hit_top] - Lz) / vz[hit_top]  # time after collision
        vz[hit_top] = -vz[hit_top]  # reverse normal component of velocity
        z[hit_top] = Lz + dt_ac * vz[hit_top]

