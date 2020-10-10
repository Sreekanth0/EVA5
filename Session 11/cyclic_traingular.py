import numpy as np
import math
import matplotlib.pyplot as plt


total_cycles = 3
step_size = 15
lr_max = 0.001
lr_min = 0.0001

def getlr_req(x_val):
    cycle = math.floor(1 + (x_val / (2 * step_size)))
    req = abs((x_val/step_size) - (2*cycle) + 1)
    lr_req = lr_min + (lr_max - lr_min) * (1 - req)
    return lr_req


x = np.linspace(0, total_cycles*step_size*2, 500)
y = np.array([getlr_req(val) for val in x])


plt.plot(x, y)
plt.xlabel('Iterations')
plt.xticks(np.arange(0,100,15))
plt.ylabel('LR')
plt.savefig('images/traingular_schedule.png')
