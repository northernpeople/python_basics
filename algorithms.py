
unsorted = [99, 3, 4, 3, 1, 9, 107, 22, 33, 44, 55, 2]


def selection_sort(ray):

    for i in range(0, len(ray ) -1):
        # select smallest in unsorted part
        smallest = ray[i]
        smallestIndex = i
        for j in range(i, len(ray)):
            if ray[j] < smallest:
                smallestIndex = j
                smallest = ray[j]
        ray[smallestIndex], ray[i] = ray[i], ray[smallestIndex]
    return ray

print selection_sort(unsorted)
