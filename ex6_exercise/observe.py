import numpy as np
from color_histogram import color_histogram
from chi2_cost import chi2_cost
import math

def observe(particles, frame, bbox_height, bbox_width, hist_bin, hist, sigma_observe):
    weights = []
    print("observe")
    print(frame.shape)

    for i in range(particles.shape[0]):
        xmin = particles[i,0] - int(bbox_width/2)
        xmax = particles[i,0] + int(bbox_width/2)
        ymin = particles[i,1] - int(bbox_height/2)
        ymax = particles[i,1] + int(bbox_height/2)
        if xmax > frame.shape[1] - 1:
            xmax = frame.shape[1] - 1
        if xmin < 0:
            xmin = 0
        if ymax > frame.shape[0] - 1:
            ymax = frame.shape[0] - 1
        if ymin < 0:
            ymin = 0      
        color_hist = color_histogram(xmin,ymin,xmax,ymax,frame, hist_bin)
        #print(hist,color_hist)
        dist = chi2_cost(hist , color_hist)
        #print(dist)

        weight = 1 / (np.sqrt(math.pi * 2) * sigma_observe) * np.exp(-(dist/sigma_observe) ** 2 / 2) 
        #print(weight)
        weights.append(weight)
    
    weights = np.array(weights)
    
    weights = weights / (np.sum(weights))
    #print(weights)
    #print(weights.sum())

    return weights



