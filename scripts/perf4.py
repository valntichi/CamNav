import sys, time

N = 2000000
x = list()
start = time.time()
for i in range(100):
    line = list()
    for j in range(N):
        line.append(0.0)
    x.append(line)
end = time.time()
print (sys.getsizeof(x))
print(end - start)