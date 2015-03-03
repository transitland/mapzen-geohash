"""geohash unit tests."""
import unittest
import tempfile
import zipfile
import glob
import os
import json

import geohash

class TestGeoHash(unittest.TestCase):
  test_geohashes = [
    ['xn76urwe1g9y', (139.76608408614993, 35.681382017210126)],
    ['9q8yykv7bpr4', (-122.41343496367335, 37.775799008086324)],
    ['qgmpv9mkv4x0', (131.03038312867284, -25.34874997101724)]
  ]

  def test_decode(self):
    for test, expect in self.test_geohashes:
      value = geohash.decode(test)
      self.assertAlmostEqual(value[0], expect[0])
      self.assertAlmostEqual(value[1], expect[1])
  
  def test_encode(self):
    for expect, test in self.test_geohashes:
      value = geohash.encode(test)
      self.assertAlmostEqual(value[0], expect[0])
      self.assertAlmostEqual(value[1], expect[1])
      
  def test_roundtrip(self):
    for test, expect in self.test_geohashes:
      encoded = geohash.decode(test)
      decoded = geohash.encode(encoded)
      assert test == decoded
  
  def test_neighbors(self):
    test = '9p'
    expect = {'s': '9n', 'e': '9r', 'w': '8z', 'nw': 'bb', 'sw': '8y', 'ne': 'c2', 'se': '9q', 'n': 'c0', 'c':'9p'}
    result = geohash.neighbors(test)
    for k in expect:
      assert expect[k] == result[k]

  def test_adjacent(self):
    assert geohash.adjacent('9p', 'e') == '9r'
    assert geohash.adjacent('9p', 's') == '9n'
    assert geohash.adjacent('9p', 'w') == '8z'
    assert geohash.adjacent('9p', 'n') == 'c0'
      
if __name__ == '__main__':
    unittest.main()