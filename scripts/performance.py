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

from matter_allocation.models import *

__list = ['4769427012', '4769427011', '2672705003', '2672705004', '2672705001', '2672705006',
          '75016100368', '10849107002', '10849107004', '10849107003', '7519298001', '7519298004', '7519298006',
          '75005696782', '7519298005', '75001596895', '5609613009', '44050045012804', '44050045012805',
          '44050045012803',
          '9517915E001', '9517915E002', '2888197004', '2888197011', '2888197013', '2888197005', '9142951E002',
          '9142951E005', ]

for a in AllocationHandOver.objects.filter(account_number__in=__list):
    a.current_reason_code = '303'
    a.previous_reason_code = '312'
    a.save()

for a in AllocationHandOver.objects.filter(project_code='110'):
    a.current_reason_code = '303'
    a.previous_reason_code = '307'
    a.save()

from project.models import *
for a in Account.objects.filter(project_id=156):
    a.current_reason_code = '303'
    a.previous_reason_code = '307'
    a.save()
