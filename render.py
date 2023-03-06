import pandas as pd
import cv2 as cv
import numpy as np
import statistics as stat

def render(verts2d, faces, vcolors, depth, shade_t):

    #Image dimensions
    M = 512 
    N = 512

    #Number of triangles:
    k = len(faces)
    
    #initialize image:
    img = np.ones((M,N,3))

    triangle_depth = np.zeros(k)

    for j in range (k):
         triangle_depth[j] = (stat.mean(depth[faces[j][0]] + depth[faces[j][1]] + depth[faces[j][2]]))



    #sort the depth array
    depth = np.sort(depth)[::-1]



    return img