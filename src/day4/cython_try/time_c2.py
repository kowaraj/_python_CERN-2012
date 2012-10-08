import timeit  

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000

t = timeit.Timer("c2.great_circle(%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2), "import c2")
print "Cython function (using trig function from math.h)", t.timeit(num), "sec"

