import numpy as np
from scipy.stats import norm


def propagate(particles, frame_height, frame_width, params):
    A = np.eye(particles.shape[1])
    print("propagate")
    print(particles.shape)
    print(frame_width, frame_height)
    noise = np.zeros(particles.shape)
    new_samp = []
    if particles.shape[1] > 2:
        A[:2,2:4] += np.eye(2)
        noise[:, 2:4] += np.random.normal(0, params['sigma_velocity'], noise[:, 2:4].shape)
        print(A)

    noise[:, :2] += np.random.normal(0, params['sigma_velocity'], noise[:, :2].shape)
    new_samp = np.transpose(A.dot(particles.T)) + noise

    for i in range(0, new_samp.shape[0]):
        new_samp[i, 0] = 0 if new_samp[i,0] < 0 else new_samp[i, 0]
        new_samp[i, 0] = frame_width - 1 if new_samp[i,0] >=frame_width else new_samp[i, 0]
        new_samp[i, 1] = 0 if new_samp[i,1] < 0 else new_samp[i, 1]
        new_samp[i, 1] = frame_height - 1 if new_samp[i,1] >=frame_height else new_samp[i, 1]

    return new_samp

