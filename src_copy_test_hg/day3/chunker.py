def chunk(n, iterable):
    iterator = iter(iterable)
    while True:
        yield [iterator.next() for _ in xrange(n)]

for a,b,c in chunk(3,'123456789'):
    print a,b,c
