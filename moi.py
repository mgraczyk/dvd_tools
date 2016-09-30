from datetime import datetime
import struct

class MoiData(object):
  __slots__ = ("_version", "_dt", "_duration")

  def __init__(self, version, dt, duration):
    self._version = version
    self._dt = dt
    self._duration = duration

  @property
  def version(self):
    return self._version

  @property
  def datetime(self):
    return self._dt

  @property
  def duration(self):
    return self._duration

  @classmethod
  def decode_file_path(cls, path):
    with open(path, "rb") as f:
      return cls.decode_file(f)

  @classmethod
  def decode_file(cls, f):
    (version,
     filesize,
     year, month, day, hour, minutes, milliseconds,
     duration) = struct.unpack(
        '!2sIHBBBBHI', f.read(18))

    seconds = milliseconds / 1000
    microseconds = 1000 * (milliseconds - 1000*seconds)

    dt = datetime(year, month, day, hour, minutes, seconds, microseconds)

    return MoiData(version, dt, duration)
