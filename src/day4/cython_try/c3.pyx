cdef extern from "math.h":
    float cosf(float theta)
    float sinf(float theta)
    float acosf(float theta)

cdef float _great_circle_internal(float lon1,float lat1,float lon2,float lat2):
    cdef float radius = 3956.0 
    cdef float pi = 3.14159265
    cdef float x = pi/180.0
    cdef float a,b,theta,c

    a = (90.0-lat1)*(x)
    b = (90.0-lat2)*(x)
    theta = (lon2-lon1)*(x)
    c = acosf((cosf(a)*cosf(b)) + (sinf(a)*sinf(b)*cosf(theta)))
    return radius*c

def great_circle33(float lon1,float lat1,float lon2,float lat2,int num):
    cdef int i
    cdef float x
    print 'c33.great_circle: num = ', num
    for i from 0 <= i < num:
        x = _great_circle_internal(lon1,lat1,lon2,lat2)
    return x