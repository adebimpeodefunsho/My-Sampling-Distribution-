# Loading the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

students = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])
#simulating 10 draws from student array
sample1 = np.random.choice(students, 10, replace=True)
# getting 10,000 proportion of the above sampling distribution
sample_props = []
for _ in range(10000):
    sample = np.random.choice(students, 5, replace=True)
    sample_proppp.append(sample.mean())
sample_props = np.array(sample_props)
