import numpy as np
import matplotlib.pyplot as plt

#Initial conditions/static values
m_gas = 10**-23 #Mass of each gas particle in kg (Change later)
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
px_gas = np.random.uniform(p_gas_min, p_gas_max, num_particles)
py_gas = np.random.uniform(p_gas_min, p_gas_max, num_particles)
x0_gas = np.random.uniform(0, box_width, num_particles)
y0_gas = np.random.uniform(0, box_height, num_particles)

class Ball:
    def __init__(self, dt, x0, y0, px0, py0, r_ball, m_ball, m_gas, box_width, box_height, num_particles):
        self.dt = dt
        self.x0 = x0
        self.y0 = y0
        self.px0 = px0
        self.py0 = py0
        self.r_ball = r_ball
        self.m_ball = m_ball
        self.m_gas = m_gas
        self.box_width = box_width
        self.box_height = box_height
        self.num_particles = num_particles

    def ball_move(self):
        return 1
    
    def particle_move(self):
        return 1
    

x = x0_ball
y = y0_ball
px = px0_ball
py = py0_ball
while i < num_steps:
    iteration = Ball(dt, x, y, px, py, r_ball, m_ball, m_gas, box_width, box_height, num_particles)

    i+=1