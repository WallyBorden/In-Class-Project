import numpy as np
import matplotlib.pyplot as plt
import ballPos
import particle

#Initial conditions/static values
m_gas = 10**-22 #Mass of each gas particle in kg (Change later)
p_gas_max = 10**-20
p_gas_min = 10**-21
m_ball = 10 #Mass of ball in kg
r_ball = 1
x0_ball = 0 
y0_ball = 0
px0_ball = 0
py0_ball = 0
num_particles = 100 #Number of gas particles
box_width = 10 #m
box_height = 10 #m
g = -9.8 #m/s^2
num_steps = 100
dt = 10**-3 #s
i = 0

#Array of gas particle momentums and positions
px0_gas = np.random.uniform(p_gas_min, p_gas_max, num_particles)
py0_gas = np.random.uniform(p_gas_min, p_gas_max, num_particles)
x0_gas = np.random.uniform(0, box_width, num_particles)
y0_gas = np.random.uniform(0, box_height, num_particles)

class Ball:
    def __init__(self, dt, x0, y0, x0_gas, y0_gas, px0, py0, px0_gas, py0_gas, r_ball, m_ball, m_gas, box_width, box_height, num_particles):
        self.dt = dt
        self.x0 = x0
        self.y0 = y0
        self.x0_gas = x0_gas
        self.y0_gas = y0_gas
        self.px0 = px0
        self.py0 = py0
        self.px0_gas = px0_gas
        self.py0_gas = py0_gas
        self.r_ball = r_ball
        self.m_ball = m_ball
        self.m_gas = m_gas
        self.box_width = box_width
        self.box_height = box_height
        self.num_particles = num_particles

    def ball_move(self):
        new = ballPos()
        return new
    
    def particle_move(self):
        new = particle()
        return 1
    

x = [x0_ball]
y = [y0_ball]
px = [px0_ball]
py = [py0_ball]
x_gas = [x0_gas]
y_gas = [y0_gas]
px_gas = [px0_gas]
py_gas = [py0_gas]
while i < num_steps:
    iteration = Ball(dt, x[-1], y[-1], x_gas[-1], y_gas[-1], px[-1], py[-1], px_gas[-1], py_gas[-1], r_ball, m_ball, m_gas, box_width, box_height, num_particles)
    x_new = Ball.ball_move() #Update variables with this
    particle_x_new = Ball.particle_move()
    #Add updated variables to arrays
    i+=1

plt.figure()
plt.scatter(x, y, color="red")
plt.title("Position")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.show()

plt.figure()