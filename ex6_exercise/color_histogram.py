import numpy as np

def color_histogram(xmin, ymin, xmax, ymax, frame, hist_bin):
    hist = np.zeros((3, hist_bin))
    print(frame.shape)

    if xmax > frame.shape[1] - 1:
        xmax = frame.shape[1] - 1
    if xmin < 0:
        xmin = 0
    if ymax > frame.shape[0] - 1:
        ymax = frame.shape[0] - 1
    if ymin < 0:
        ymin = 0

    for x in range(int(xmin), int(xmax)):
        for y in range(int(ymin), int(ymax)):
            color = frame[y][x] / hist_bin
            #print(color)
            for i in range(3):
                hist[i,int(color[i])] += 1
    #print(hist)
    return hist/hist.sum()