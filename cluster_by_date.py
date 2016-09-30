#!/usr/bin/env python

from __future__ import print_function

from collections import namedtuple
import glob
import json
import os
import sys

import numpy as np
import matplotlib.pyplot as plt

from moi import MoiData
from optimize import optimize

MoiFile = namedtuple("MoiFile", ("path", "size", "data"))

def get_sizes(path):
  with open(path, "r") as f:
    return json.load(f)

def get_path_key(path):
  return os.path.split(os.path.dirname(path))[1] + \
      "_" + os.path.splitext(os.path.basename(path))[0]

def get_mois(path, sizes):
  paths = glob.glob(os.path.join(path, "**", "*.MOI"))
  return tuple(
      MoiFile(
        p,
        sizes[get_path_key(p)],
        MoiData.decode_file_path(p)) for p in paths)

def get_clusters(path):
  sizes = get_sizes(os.path.join(path, "sizes.json"))
  mois = get_mois(path, sizes)

  clusters = optimize(mois)

  return clusters

def main(argv):
  path = argv[1] if len(argv) > 1 else "."

  clusters = get_clusters(path)
  print(clusters)

if __name__ == "__main__":
  main(sys.argv)
