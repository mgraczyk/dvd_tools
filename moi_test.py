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

  def test_year(self):
    self.assertEqual(self.moi_data.year, 2010)

  def test_month(self):
    self.assertEqual(self.moi_data.month, 9)

  def test_day(self):
    self.assertEqual(self.moi_data.day, 3)

  def test_hour(self):
    self.assertEqual(self.moi_data.hour, 18)

  def test_minutes(self):
    self.assertEqual(self.moi_data.minutes, 28)

  def test_seconds(self):
    self.assertEqual(self.moi_data.seconds, 4)

  def test_milliseconds(self):
    self.assertEqual(self.moi_data.milliseconds, 4000)

  def test_datetime(self):
    dt = datetime(2010, 9, 3, 18, 28, 4, 0)
    self.assertEqual(self.moi_data.datetime, dt)

if __name__ == "__main__":
  unittest.main()
