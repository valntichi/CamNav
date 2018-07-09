import time
def InsertTime(keys, iterations):
    start = time.time()
    for _ in xrange(iterations):
        d = {}
        for k in keys:
            d[k] = 0
    end = time.time()
    return (end-start)/float(len(keys)*iterations)
def LookupTime(keys, iterations):
    d = {}
    for k in keys:
        d[k] = 0
    start = time.time()
    for _ in xrange(iterations):
        for k in keys:
            _ = d[k]
    end = time.time()
    return (end-start) / float(len(keys)*iterations)
class BadHash(object):
    def __hash__(self):
        return 0xbad
bad_range = lambda n: [BadHash() for _ in xrange(n)]
print "%10s %10s %10s: %s" % (
        "key type", "operation", "keys", "time/op*10**9")
for key_label, key_range, f, n in [
        ('int', range, InsertTime, 2**7),
        ('int', range, InsertTime, 2**12),
        ('int', range, InsertTime, 2**20),
        ('int', range, InsertTime, 2**25),
        ('int', range, LookupTime, 2**7),
        ('int', range, LookupTime, 2**12),
        ('int', range, LookupTime, 2**20),
        ('int', range, LookupTime, 2**25),
        ('BadHash', bad_range, InsertTime, 2**7),
        ('BadHash', bad_range, InsertTime, 2**10),
        ('BadHash', bad_range, InsertTime, 2**12),
        ('BadHash', bad_range, LookupTime, 2**7),
        ('BadHash', bad_range, LookupTime, 2**10),
        ('BadHash', bad_range, LookupTime, 2**12),
]:
    print "%10s %10s %10d: %d" % (
            key_label, f.__name__, n, f(key_range(n), 10)*10**9)
