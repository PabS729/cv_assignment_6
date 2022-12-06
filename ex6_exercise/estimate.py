import numpy as np

def estimate(particles, particles_w):
    print("estimate")
    print(particles.shape, particles_w.shape)
    print(np.transpose(particles.T.dot(particles_w)))

    return np.transpose(particles.T.dot(particles_w))