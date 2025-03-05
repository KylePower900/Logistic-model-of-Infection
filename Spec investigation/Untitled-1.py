import random
import numpy as np 


array = np.array([np.zeros(1000000000), np.ones(1000000000)])
print(array.sum(axis=0))