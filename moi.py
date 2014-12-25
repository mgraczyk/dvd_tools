from datetime import datetime
import struct

class MoiData(object):
  __slots__ = ("_version", "_dt")

  def __init__(self, version, dt):
    self._version = version
    self._dt = dt

  @property
  def version(self):
    return self._version

  @property
  def datetime(self):
    return self._dt

  @property
  def year(self):
    return self._dt.year

  @property
  def month(self):
    return self._dt.month

  @property
  def day(self):
    return self._dt.day

  @property
  def hour(self):
    return self._dt.hour

  @property
  def minutes(self):
    return self._dt.minute

  @property
  def seconds(self):
    return self._dt.second

  @property
  def milliseconds(self):
    return self._dt.microsecond / 1000 + self._dt.second * 1000

  @classmethod
  def decode_file_path(cls, path):
    with open(path, "rb") as f:
      return cls.decode_file(f)

  @classmethod
  def decode_file(cls, f):
    version, = struct.unpack('!2s', f.read(2))

    # filesize in bytes
    f.read(4)

    year, month, day, hour, minutes, milliseconds = struct.unpack(
        '!HBBBBH', f.read(8))

    seconds = milliseconds / 1000
    microseconds = 1000 * (milliseconds - 1000*seconds)

    dt = datetime(year, month, day, hour, minutes, seconds, microseconds)

    return MoiData(version, dt)



