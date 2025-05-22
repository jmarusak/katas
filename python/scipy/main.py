import sys
import numpy as np
from scipy.stats import skew

def round0(n):
    return round(n, 0)

def round1(n):
    return round(n, 1)

def round2(n):
    return round(n, 2)

def round3(n):
    return round(n, 3)

def number_of_classes(n):
    k = np.log2(n) / np.log2(2)
    k = np.ceil(k)
    return k

def class_interval(data):   
    min_value = np.min(data)
    max_value = np.max(data)
    interval = (max_value - min_value) / number_of_classes(data.size)
    interval = np.ceil(interval)
    return interval

# Read cli parameter ddof into a variable
ddof = int(sys.argv[1]) if len(sys.argv) > 1 else 1

# Load dataset to numpy array
data = np.loadtxt('dataset.txt', delimiter=',')
data.sort()
print("data:", data)

# Enumerate the data and print the values
for i, value in enumerate(data):
    print(value)

print()
size = data.size
print("size:", size)

min = np.min(data)
print("min:", min)

max = np.max(data)
print("max:", max)

range = max - min
print("range:", range)


print()
mean = np.mean(data)
print("mean:", round2(mean))

median = np.median(data)
print("median:", round2(median))

mode = np.argmax(np.bincount(data.astype(int)))
print("mode:", mode)

var = np.var(data, ddof=ddof)
print("var:", round2(var))

std = np.std(data, ddof=ddof)
print("std:", round2(std))


print()
q1 = np.percentile(data, 25, method='weibull')
print("q1:", round2(q1))

q3 = np.percentile(data, 75, method='weibull')
print("q3:", round2(q3))

iqr = q3 - q1
print("iqr:", round2(iqr))

lower_bound = q1 - 1.5 * iqr
print("lower_bound:", round2(lower_bound))

upper_bound = q3 + 1.5 * iqr
print("upper_bound:", round2(upper_bound))


print()
pskew = 3 * (mean - median) / std
print("pskew:", round3(pskew))

sskew = skew(data, bias=False)
print("sskew:", round3(sskew))

print()
nclasses = number_of_classes(size)
print("nclasses:", round0(nclasses))

interval = (max - min) / nclasses
interval = np.ceil(interval / 5) * 5
print("interval:", round2(interval))

if ddof == 0:
    print("\nThis is a population!")
else:
    print("\nThis is a sample!")
