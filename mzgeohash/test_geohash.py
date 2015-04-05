"""geohash unit tests."""
import unittest
import tempfile
import zipfile
import glob
import os
import json

import geohash

class Test_encode_decode(unittest.TestCase):
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

class Test_neighbors(unittest.TestCase):
  def test_neighbors(self):
    test = '9p'
    expect = {'s': '9n', 'e': '9r', 'w': '8z', 'nw': 'bb', 'sw': '8y', 'ne': 'c2', 'se': '9q', 'n': 'c0', 'c':'9p'}
    result = geohash.neighbors(test)
    for k in expect:
      assert expect[k] == result[k]

class Test_adjacent(unittest.TestCase):
  def test_adjacent(self):
    assert geohash.adjacent('9p', 'e') == '9r'
    assert geohash.adjacent('9p', 's') == '9n'
    assert geohash.adjacent('9p', 'w') == '8z'
    assert geohash.adjacent('9p', 'n') == 'c0'
      
class Test_neighborsfit(unittest.TestCase):
  test_centroid = [-122.18472385000001, 37.7881345]
  test_points = [
    (-122.2992715, 37.9030588),
    (-122.396742, 37.792976),
    (-122.4474142, 37.72198087),
    (-121.9764, 37.557355),
    (-122.029095, 37.973737),
    (-122.224274, 37.774963),
    (-122.271604, 37.803664),
    (-122.126871, 37.697185),
    (-122.087967, 37.670399),
    (-122.123801, 37.893394),
    (-122.269029, 37.80787),
    (-122.265609, 37.797484),
    (-122.267227, 37.828415),
    (-122.067423, 37.905628),
    (-122.267227, 37.828415),
    (-122.38666, 37.599787),
    (-122.075567, 37.690754),
    (-122.401407, 37.789256),
    (-122.283451, 37.87404),
    (-122.269029, 37.80787),
    (-122.1837911, 37.87836087),
    (-122.419694, 37.765062),
    (-122.2945822, 37.80467476),
    (-122.21244024, 37.71297174),
    (-121.945154, 38.018914),
    (-122.466233, 37.684638),
    (-122.056013, 37.928403),
    (-122.406857, 37.784991),
    (-122.418466, 37.752254),
    (-122.26978, 37.853024),
    (-122.251793, 37.844601),
    (-121.928099, 37.699759),
    (-122.416038, 37.637753),
    (-122.1613112, 37.72261921),
    (-122.0575506, 37.63479954),
    (-122.392612, 37.616035),
    (-122.413756, 37.779528),
    (-122.353165, 37.936887),
    (-122.197273, 37.754006),
    (-122.017867, 37.591208),
    (-122.024597, 38.003275),
    (-122.4690807, 37.70612055),
    (-122.268045, 37.869867),
    (-122.444116, 37.664174),
    (-121.900367, 37.701695),
    (-122.317269, 37.925655),
    (-122.434092, 37.732921)
    ]
    
  def test_neighborsfit(self):
    expect = '9q9'
    assert geohash.neighborsfit(self.test_centroid, self.test_points) == expect
      
