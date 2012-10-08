import timeit  

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 500000


t = timeit.Timer("_c333.great_circle333(%f,%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2,num), "import _c333")

print "Cython function (single call with a param num) :", t.timeit(1), "sec"










