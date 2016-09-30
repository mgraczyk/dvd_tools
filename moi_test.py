#!/usr/bin/env python

from datetime import datetime
import glob
import os
import unittest

from moi import MoiData

test_path = os.path.join("testdata", "MOV01F.moi")

class MoiDataTest(unittest.TestCase):

  def setUp(self):
    self.moi_data = MoiData.decode_file_path(test_path)

  def test_version(self):
    self.assertEqual(self.moi_data.version, "V6")

  def test_datetime(self):
    dt = datetime(2010, 9, 3, 18, 28, 4, 0)
    self.assertEqual(self.moi_data.datetime, dt)

  def test_duration(self):
    self.assertEqual(self.moi_data.duration, 99599)

if __name__ == "__main__":
  unittest.main()
