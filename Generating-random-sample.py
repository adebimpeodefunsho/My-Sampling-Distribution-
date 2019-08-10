# Loading the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

fraud = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1,0])
#simulating 10 draws from fraud array
sample1 = np.random.choice(fraud, 10, replace=True)
# getting 10,000 iterations of the above sampling distribution
sample_props = []
for _ in range(10000):
#this generates 5 draws from the fraud numpy array
    sample = np.random.choice(fraud, 5, replace=True)
    sample_props.append(sample.mean())
    sample_props = np.array(sample_props)
