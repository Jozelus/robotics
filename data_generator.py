#import numpy as np
import random

n = 100

data_file = open("data.txt", 'w')

for i in range(n):
    data_file.write(str(random.randint(0, 9)))
    data_file.write(' ')
    data_file.write(str(random.randint(0, 1)))
    data_file.write('\n')

data_file.close()

