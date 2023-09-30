import numpy as np
import matplotlib.pyplot as plt
import math
import random

k = 10
vertices = np.linspace(1,10000,10000)
vertices = vertices.astype(int)
A = []
for i in range(k):
    A.append([])
A[0] = vertices


for i in range(1,k):
    probability = math.pow(len(vertices),-1/k)
    for i1 in range(len(A[i-1])):
        rand = random.random()
        if rand <= probability:
            A[i].append(A[i-1][i1])

lens = []
expected_lens = []
for i in A:
    lens.append(len(i))

for i in range(k):
    expected_lens.append(math.pow(len(vertices),1-i/k))

fig = plt.figure()
ax1 = fig.add_subplot()

print(lens)
print(expected_lens)

ax1.plot(lens, label='Actual lengths',c='r')
ax1.plot(expected_lens, label='Expected lengths',c='b')
plt.show()

plt.bar(np.linspace(1,len(A),len(A)), height=lens)
plt.show()