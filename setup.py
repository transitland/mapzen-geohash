from distutils.core import setup

import mzgeohash

setup(
  name='mzgeohash',
  version=mzgeohash.__version__,
  description='Mapzen Geohash',
  author='Ian Rees',
  author_email='ian@mapzen.com',
  url='https://github.com/transitland/mapzen-geohash',
  license='License :: OSI Approved :: MIT License',
  packages=['mzgeohash']
)