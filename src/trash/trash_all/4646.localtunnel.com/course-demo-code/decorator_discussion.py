from time import sleep

def memo(fn):
    cache = {}
    def proxy(*args):
        if args not in cache:
            cache[args] = fn(*args)
        return cache[args]
    return proxy

def slow_add(a,b):
    sleep(3)
    return a+b

def slow_mul(a,b):
    return a*b

fast_add = memo(slow_add)

def div(a,b):
    sleep(3)
    return a/b
div = memo(div)

def paint(...):
    ...

filtered_green_paint = filter_colour(green)(paint)
filtered_green_paint = filter_colour(green, paint)
filtered_blue_paint  = filter_colour(blue, paint)

@filter(green)
def paint(...):
    ...
# paint = filter(green)(paint)
