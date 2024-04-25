import numpy as np

a = np.array([[-0.25 ,-0.25, -0.25],
 [-0.25,  0.25,  0.25],
 [ 0.25, -0.25,  0.25],
 [ 0.25,  0.25, -0.25]])
tetr_void = np.array([
    [0.25, 0.25, 0.25],
    [0.25, 0.75, 0.75],
    [0.75, 0.25, 0.75],
    [0.75, 0.75, 0.25],
    [0.75, 0.75, 0.75],
    [0.75, 0.25, 0.25],
    [0.25, 0.75, 0.25],
    [0.25, 0.25, 0.75]
])

three_layer = np.array([
    [0, 0, 0],
    [0, 0.5, 0.5],
    [0.5, 0, 0.5],
    [0.5, 0.5, 0]
])
d = np.array([0.25, 0.25 ,0.25])

print(np.array_equal(a + d, three_layer) or np.array_equal(a - d, three_layer))