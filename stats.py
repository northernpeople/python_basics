import sys, math


def mean(ray):
    if len(ray) == 0:
        return 0
    total = 0.0
    for i in ray:
        total += i
    return total / len(ray)


def median(ray):
    sorted_ray = sorted(ray)
    length = len(ray)
    median = sorted_ray[length // 2]
    if length % 2 == 0:  # even
        median = sorted_ray[length // 2] + sorted_ray[length // 2 + 1] / 2.0
    return median


def pair_sort_key(t):
    print t
    # return t[1]
    return 1


def mode(ray):
    number_count = {}
    for i in ray:
        if not i in number_count:
            number_count[i] = 0
        number_count[i] += 1
    sorted_number_count = sorted(number_count.items(), key=lambda t: t[1], reverse=True)
    return sorted_number_count[0][0]


def variance(ray):
    ray_mean = mean(ray)
    diff_squared_sum = 0
    for i in ray:
        diff_squared_sum += (i - ray_mean) ** 2
    return diff_squared_sum / (len(ray) - 1)


def standard_deviation(ray):
    return math.sqrt(variance(ray))


def covariance(r1, r2):
    """ only sign is important, strength of connection is calculated using correlation"""
    if len(r1) != len(r2):
        return 0
    if len(r1) <= 1:
        return 0
    r1_mean = mean(r1)
    r2_mean = mean(r2)
    mean_differences_product_sum = 0.0
    for i in range(0, len(r1)):
        mean_differences_product_sum += (r1[i] - r1_mean) * (r2[i] - r2_mean)
    return mean_differences_product_sum / (len(r1) - 1)


def correlation(r1, r2):
    return covariance(r1, r2) / (standard_deviation(r1) * standard_deviation(r2))


print mean([25, 25, 100])
print median([9, 1, 2, 3, 5, 8])
print mode([9, 1, 2, 2, 3, 3, 5, 8])
print variance([1, 2, 3, 4, 5])
print standard_deviation([1, 2, 3, 4, 5])
print covariance([2.1, 2.5, 4.0, 3.6], [8, 12, 14, 10])  # must be 1.533
print covariance([1, 2, 3, 4], [4, 3, 2, 1])
print covariance([4, 3, 2, 1], [1, 2, 3, 4])
print covariance([1, 2, 3, 4], [1, 2, 3, 4])
print covariance([4, 3, 2, 1], [4, 3, 2, 1])
print correlation([4, 3, 2, 1], [1, 2, 2, 1])

sys.exit(0)
