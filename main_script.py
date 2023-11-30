import numpy as np
import matplotlib.pyplot as plt

#Initial conditions/static values
m_gas = 1 #Mass of each gas particle in kg (Change later)
m_ball = 10 #Mass of ball in kg
x0_ball = 0 
y0_ball = 0
vx0_ball = 0
vy0_ball = 0
num_particles = 100 #Number of gas particles
#Need to initial each particle with a random position
box_width = 10 #m
box_height = 10 #m
g = -9.8 #m/s^2