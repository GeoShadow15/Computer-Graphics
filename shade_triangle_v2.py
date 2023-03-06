import math
import numpy as np
import pandas as pd


# -----------------------------------------------------------------
# The variables of the shade_triangle function are presented below:


# img : an array (image) with M x N x 3 dimensions 

# verts2d : 3 x 2 array filled with integers. Each row represents the 2-dimension coordinates of a triangle's vertices

# vcolors : 3 x 3 array filled with floats between [0,1]. Each row represents the 3 color components (RGB) of each triangle's vertex.

# shade_t : string variable. Possible values are "flat" or "gouraud". It differentiates the method used to fill the triangles with color.

# Y : the returned value of the function. An M x N x 3 array, that contains the RGB values of each point in the M x N triangle grid.

# -----------------------------------------------------------------






def shade_triangle(img, verts2d, vcolors, shade_t):


    #------
    # FLAT 
    #------
   if shade_t == 'flat' :
    
        (vcolors[0] + vcolors[1] + vcolors[3]) / 3
         
        k = 3

        #Calculate xkmin, xkmax, ykmin, ykmax for each of the 3 triangle sides.

        #--------------
        #Side 1 (k = 1)
        # x1min and x1max
        if verts2d[0][0] >= verts2d[1][0] :
            x1min = verts2d[1][0]
            x1max = verts2d[0][0]
        elif verts2d[0][0] <= verts2d[1][0] :
            x1min = verts2d[0][0]
            x1max = verts2d[1][0]

        # y1min and y1max
        if verts2d[0][1] >= verts2d[1][1] :
            y1min = verts2d[1][1]
            y1max = verts2d[0][1]
        elif verts2d[0][1] <= verts2d[1][1] :
            y1min = verts2d[0][1]
            y1max = verts2d[1][1]

        #--------------
        #Side 2 (k = 2)
        # x2min and x2max
        if verts2d[1][0] >= verts2d[2][0] :
            x2min = verts2d[2][0]
            x2max = verts2d[1][0]
        elif verts2d[1][0] <= verts2d[2][0] :
            x2min = verts2d[1][0]
            x2max = verts2d[2][0]

        # y2min and y2max
        if verts2d[1][1] >= verts2d[2][1] :
            y2min = verts2d[2][1]
            y2max = verts2d[1][1]
        elif verts2d[1][1] <= verts2d[2][1] :
            y2min = verts2d[1][1]
            y2max = verts2d[2][1]

        #--------------
        #Side 3 (k = 3)
        # x3min and x3max
        if verts2d[2][0] >= verts2d[0][0] :
            x3min = verts2d[0][0]
            x3max = verts2d[2][0]
        elif verts2d[2][0] <= verts2d[0][0] :
            x3min = verts2d[2][0]
            x3max = verts2d[0][0]

        # y3min and y3max
        if verts2d[2][1] >= verts2d[0][1] :
            y3min = verts2d[0][1]
            y3max = verts2d[2][1]
        elif verts2d[2][0] <= verts2d[0][1] :
            y3min = verts2d[2][1]
            y3max = verts2d[0][1]
         #--------------   
        
        #Calculate ymin and ymax
        ymin = min(y1min, y2min, y3min)
        ymax = max(y1max, y2max, y3max)


        #Calculate the slopes for each side that is not vertical
        if verts2d[1][0] != verts2d[0][0]:
            m1 = (verts2d[1][1] - verts2d[0][1]) / (verts2d[1][0] - verts2d[0][0])
        
        if verts2d[2][0] != verts2d[1][0]:
            m2 = (verts2d[2][1] - verts2d[1][1]) / (verts2d[2][0] - verts2d[1][0])

        if verts2d[0][0] != verts2d[2][0]:    
            m3 = (verts2d[0][1] - verts2d[2][1]) / (verts2d[0][0] - verts2d[2][0])

        
        for y in range (ymin,ymax,1):         
            







    
    
    
    
    
    
    return Y
