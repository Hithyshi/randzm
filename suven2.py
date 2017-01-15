import matplotlib.pyplot as plt
import numpy as np
estimated_populations=[12, 15, 98, 109, 210, 300, 450, 500, 550, 320, 440, 590, 623, 678, 753, 803, 879, 950, 1040, 1209, 1320, 1425 1498, 444, 333, 212, 450, 599, 233, 1227, 306]

bins=[0, 100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500]

ply.hist(estimated_populations, bins, histtype='bar')

plt.xlabel("Population ranges in millions")
plt.ylabel("Distribution frequency of population)
plt.title("Distribution of Estimated population of different countries")
plt.show()

hist,bin_edges = (np.histogram(estimated_populations, bins))

mydict=dict(zip(bin_edges[0]),hist[0])

for k,v in mydict.iteritems():
	print k, v