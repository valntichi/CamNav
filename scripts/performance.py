import requests
from threading import Thread

from multiprocessing import Pool
results = {}
def get_home(i):
    r = requests.get('http://localhost:8011/')
    results[i] = r

i = 0
# t = Thread(target=get_home, args=(1,))
# t.start()
# t.join()
# print results

while i < 2000000:
    t = Thread(target=get_home, args=(i,))
    t.start()
    if i % 100 == 0:
        t.join()
        print i, results[i]

    i += 1

# hitting the website with 50 concurrent users
concurrent = 50

# with Pool(processes=10) as pool:
#     result =  pool.apply(get_home,())
#     print result
"""
load testing with locust?

"""