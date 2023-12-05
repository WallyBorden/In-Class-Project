import numpy as np


def BallPosition(particlePx, particlePy, particleX, particleY, ballPx, ballPy, ballX, ballY, ballM, particleM, ballR):
    
    ballx_new = ballPx/ballM*dt
    bally_new = ballPy/ballM*dt

    delta_px = []
    delta_py = []
    particle_Px_new = []
    particle_Py_new = []
    
    for i in range(len(particlePx)):
        if abs(particleX[i]-ballx_new) > ballR and abs(particleY[i]-bally_new) > ballR:
            energy_tot = (particlePx[i]**2 + particlePy[i]**2)/(2*particleM) + (ballPx**2 + ballPy**2)/(2*ballM)
            momX_tot = particlePx[i] + ballPx[i]
            momY_tot = particlePy[i] + ballPy[i]
            particleMom_tot = np.sqrt(particlePx[i]**2 + particlePy[i]**2)
            
            particle_angle = np.arcsin(particlePy[i]/particleMom_tot)

            

            
            
        
