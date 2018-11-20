unsorted = [99, 3, 4, 3, 1, 9, 107, 22, 33, 44, 55, 2]


# best case: first item is the one that we are looking for
# worst case: we checked all array, item not found
def linear_search(ray, value):
    for i in range(0, len(ray)):
        if ray[i] == value:
            return i
    return -1


# best case: first item we look at
# worst case: log n operations and item not found
def binary_search(ray, value):
    print ray, value
    ray_length = len(ray)

    if ray_length == 0:
        return False
    if ray_length == 1:
        return ray[0] == value

    middle_index = ray_length // 2

    if ray[middle_index] == value:
        return True
    else:
        if value < ray[middle_index]:
            return binary_search(ray[:middle_index], value)
        else:
            return binary_search(ray[middle_index:], value)


# best case: n^2 worst case: n^2, best and worst are the same: big Theta of n^2
def selection_sort(ray):
    for i in range(0, len(ray)):
        smallest_index = i
        for j in range(i, len(ray)):
            if ray[j] < ray[smallest_index]:
                smallest_index = j
        ray[i], ray[smallest_index] = ray[smallest_index], ray[i]
    return ray


# best case: sorted array takes n steps
# worst case: reversed array takes n^2
def insertion_sort(ray):
    for i in range(1, len(ray)):
        j = i
        while j > 0 and ray[j - 1] > ray[j]:
            print ray
            ray[j - 1], ray[j] = ray[j], ray[j - 1]
            j -= 1
    return ray


# print selection_sort(unsorted)
print insertion_sort(unsorted)
# print insertion_sort([5, 4, 3, 2, 1])
# print insertion_sort([-1, -2, 0, 5, 0])

# print linear_search(unsorted, 22)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 22)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 2)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 3)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 10)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 11)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 13)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 0)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 1)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 4)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 5)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 6)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 9)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 12)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 23)
# print binary_search([1, 4, 5, 6, 8, 9, 12, 23, 24], 24)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 0)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 2)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 3)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 7)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 8)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 11)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 13)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 4)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 5)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 6)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 9)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 12)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 23)
# print binary_search([1, 4, 5, 6, 9, 12, 23, 24], 24)
# print binary_search([-5, -3, -1, 1, 2, 4, 7], -7)
# print binary_search([-5, -3, -1, 1, 2, 4, 7], 0)
# print binary_search([-5, -3, -1, 1, 2, 4, 7], -1)
# print binary_search([-5, -3, -1, 1, 2, 4, 7], 3)
# print binary_search([-5, -3, -1, 1, 2, 4, 7], 4)
# print binary_search([], -4)
