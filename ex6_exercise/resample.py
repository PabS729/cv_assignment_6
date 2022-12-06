import numpy as np
from numpy.random import choice
from observe import observe

def resample(particles, particles_w):
    print("resample")
    idx = np.linspace(0, particles.shape[0]-1, particles.shape[0], dtype=int)
    sp = choice(idx, size = particles.shape[0], replace = True, p=particles_w)

    new_sample = particles[sp]
    new_weights = particles_w[sp] / particles_w[sp].sum()

    return new_sample, new_weights

    