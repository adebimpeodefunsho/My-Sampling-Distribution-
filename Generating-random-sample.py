import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

students = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])
#simulating 10 draws from student array
sample1 = np.random.choice(students, 10, replace=True)
