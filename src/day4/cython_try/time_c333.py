import timeit  

lon1, lat1, lon2, lat2 = -72.345, 34.323, -61.823, 54.826
num = 5
num2 = 10000

t = timeit.Timer("_c334.great_circle333(%f,%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2,num), "import _c334")

print "Cython function (single call with a param num) :", t.timeit(10000), "sec"

t = timeit.Timer("_c334.great_circle333(%f,%f,%f,%f,%f)" % (lon1,lat1,lon2,lat2,num), "import _c334")

print "Cython function (single call with a param num) :", t.timeit(10000), "sec"









