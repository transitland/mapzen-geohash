# Mapzen Geohash

```
>>> import mzgeohash
>>> mzgeohash.decode('xn76urwe1g9y')
(139.76608408614993, 35.681382017210126)
>>> mzgeohash.encode((139.76608408614993, 35.681382017210126))
'xn76urwe1g9y'
>>> mzgeohash.neighbors('xn76urwe1g9y')
{'c': 'xn76urwe1g9y',
 'e': 'xn76urwe1gdn',
 'n': 'xn76urwe1g9z',
 'ne': 'xn76urwe1gdp',
 'nw': 'xn76urwe1g9x',
 's': 'xn76urwe1g9v',
 'se': 'xn76urwe1gdj',
 'sw': 'xn76urwe1g9t',
 'w': 'xn76urwe1g9w'}
```