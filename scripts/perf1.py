import timeit

print(timeit.timeit('"-".join(str(n) for n in range(100))', number=10000))
thirdparty = dict()

# for i in range(100):
#     thirdparty[i] = []
#     for j in range(100000):
#         thirdparty[i].append(j)

print(timeit.timeit("""
thirdparty = dict()
for i in range(100):
    thirdparty[i] = []
    for j in range(100000):
        thirdparty[i].append(j)
""", number=10))