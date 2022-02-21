import numpy as np
import matplotlib.pyplot as plt

# file - bismark cov file name substring
def draw(file):
  file = f'de_{file}.deduplicated.bismark.cov'
  data = open(file, 'r').readlines()
  ndata = np.empty(len(data))
  for i, cur in enumerate(data):
    # val for histogram
    _, _, _, val, _, _ = cur.split()
    ndata[i] = float(val)

  fig, ax = plt.subplots(1, 1)
  fig.set_size_inches(16, 16)
  ax.hist(ndata, bins=25)
