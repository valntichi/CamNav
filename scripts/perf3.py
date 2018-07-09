from collections import namedtuple
import sys, random, timeit


def total_size(x):
    return sys.getsizeof(x)


Account = namedtuple('Account', "account_number id_number region town", )

x = []
for i in range(2000000):
    x.append(Account(account_number="account-"+ str(i), id_number=23456644, region=random.randint(1,100), town=random.randint(1,1000)))

print(total_size(x))
print(x[0])

# qs = Items.objects.filter(...).namedtuples('title', 'amount', 'price')
# qs = AllocationHandOver.objects.filter(is_for_allocation=True).values_list('account_number', 'outstanding_balance')
count = 0
for item in x:
    if item.region == 50:
        count += 1
print (count)