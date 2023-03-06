import pandas as pd
import numpy as np
import math 

#test

x1 = np.array([1, 2.1])
x2 = np.array([4, 8.6])

x = np.array([2.4, 5.6])

C1 = np.array([3,5,6])
C2 = np.array([30,45,5])


def interpolate_color(x1, x2, x, C1, C2):

    value = np.zeros(3)

    #calculate the distance between the two trinagle vertices
    tri_verts_dist = math.sqrt(math.pow((x2[1] - x1[1]), 2) + math.pow((x2[0] - x1[0]), 2))      

    #find the distance of x from x1 vertex 
    point_to_first_vertex_dist = math.sqrt(math.pow((x[1] - x1[1]), 2) + math.pow((x[0] - x1[0]), 2))

    #find the distance of x from x2 vertex
    point_to_second_vertex_dist = math.sqrt(math.pow((x[1] - x2[1]), 2) + math.pow((x[0] - x2[0]), 2))
    
    #find the ratio = distance of x and x1 / distance of x1 and x2
    x1_ratio = point_to_first_vertex_dist / tri_verts_dist

    #find the ratio = distance of x and x2 / distance of x1 and x2   
    x2_ratio = point_to_second_vertex_dist / tri_verts_dist

    
    #Calculate the RED component of x
    value[0] = x2_ratio * C1[0] + x1_ratio * C2[0]

    #Calculate the GREEN component of x
    value[1] = x2_ratio * C1[1] + x1_ratio * C2[1]

    #Calculate the RED component of x
    value[2] = x2_ratio * C1[2] + x1_ratio * C2[2]
    
    return value



print(interpolate_color(x1, x2, x, C1, C2))