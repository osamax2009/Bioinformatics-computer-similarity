from numpy import random 
import numpy as np 

a = np.array(['A','C','G','T'])
for i in range (10) :
    print(random.permutation(a))
