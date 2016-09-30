from cluster import KMeansClustering
import datetime
import numpy as np
from operator import itemgetter
import time

import scipy.optimize

DVD_SIZE = 4.7*1000*1000*1000

def get_moi_epoch_time(moi):
  return int(time.mktime(moi.data.datetime.timetuple()))

def get_time_distance(a, b):
  return abs(a - b)

def get_cum_size(sizes):
  sizes = np.array(sizes)
  cum_size = np.cumsum(sizes)

  return cum_size

def greedy_clusters(mois, num_clusters, max_size):
  clusters = []

  cum_size = get_cum_size(map(itemgetter(1), mois))

  cluster_indices = []

  prev_end = 0
  prev_size = 0
  idx = 0

  while idx < len(mois):
    now_size = cum_size[idx] - prev_size
    if now_size >= max_size:
      cluster_indices.append((prev_end, idx, cum_size[idx-1] - prev_size))
      prev_end = idx
      prev_size = cum_size[idx]

    idx += 1

  cluster_indices.append((prev_end, idx, cum_size[idx-1] - prev_size))

  return cluster_indices

def do_optimization(_):
  improvement = float("inf")
  while improvement:
    improvement = 0

  return []

def optimize(mois):
  x = np.array(map(get_moi_epoch_time, mois))

  clusters = greedy_clusters(mois, 11, DVD_SIZE)

  points = [(v, 0) for v in x]

  #mois = sorted(mois, key=lambda moi: moi.data.duration)
  #x = np.array([moi.data.duration for moi in mois])

  # the histogram of the data
  #n, bins, patches = plt.hist(x, 200, normed=1, facecolor='green', alpha=0.75)

  #plt.xlabel('Time')
  #plt.ylabel('Quantity')
  #plt.title(r'$\mathrm{Histogram\ of\ Movie Time:}\ $')
  #plt.axis([40, 160, 0, 0.03])
  #plt.grid(True)

  #plt.show()

  #plt.plot(x)
  #plt.show()

  return clusters
