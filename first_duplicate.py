# Problem:  find the first duplicate in an integer array, where the elements can have any value between 1 and the
#           array length, else return -1
# Three solutions:
#       - adding a dict where we store unique values, until a value has been encountered again, whereupon value and
#       index are returned - O(n) time complexity;

#       - using the absolute value of an array element as the index minus 1, we set the array element at this position
#       to its negative value. If furtheron we encounter the same value, and using it as an index we find a negative
#       element in the array, we have found our first duplicate - O(n) time complexity;

#       - brute force approach. Using a nested for-loop we compare the values to the one currently pointed at by the
#       outer for-loop - O(n^2) time complexity.


from collections import defaultdict
from time import time
from random import randrange


def measure_time(fn):
    def wrapper(*args, **kwargs):
        start = time()
        fn(*args, **kwargs)
        end = time()
        return end - start

    return wrapper


def generate_array():
    return [randrange(0, 1000) for _ in range(1000)]


@measure_time
def linon(ar):                      # O(n) time complexity, added space complexity
    d = defaultdict(int)
    for idx, val in enumerate(ar):
        if val not in d:
            d[val] = idx
        else:
            return val, idx
    return -1


@measure_time
def linon_no_space(ar):             # O(n) time complexity, no added space complexity, mutates the array
    for val in ar:
        idx = abs(val) - 1
        if ar[idx] < 0:
            return val, idx
        ar[idx] = -val
    return -1


@measure_time
def sqnon(ar):                      # O(n^2) time complexity
    min_duplicate_index = len(ar)
    min_duplicate_value = None
    for i in range(len(ar)):
        for j in range(i + 1, len(ar)):
            if ar[j] == ar[i]:
                min_duplicate_index = j
                min_duplicate_value = ar[j]
    return min_duplicate_index, min_duplicate_value if min_duplicate_value else -1


def main():
    sqnon_times = []
    linon_times = []
    linon_no_space_times = []
    for run in range(1000):
        array = generate_array()
        sqnon_times.append(sqnon(array))
        linon_times.append(linon(array))
        linon_no_space_times.append(linon_no_space(array))

    sqnon_average = sum(sqnon_times) / 1000
    linon_average = sum(linon_times) / 1000
    linon_no_space_average = sum(linon_no_space_times) / 1000

    linon_str = f"Mean run time for 1000 randomly generated arrays of 1000" \
                f" elements for linear complexity solution is {linon_average:.4f} seconds"
    linon_no_space_comp_str = f"Mean run time for 1000 randomly generated arrays of 1000" \
                              f" elements for linear complexity solution without added space complexity" \
                              f" is {linon_no_space_average:.4f} seconds"
    sqnon_str = f"Mean run time for 1000 randomly generated arrays of 1000" \
                f" elements for square of n complexity solution is {sqnon_average:.4f} seconds"

    print(linon_str)
    print(linon_no_space_comp_str)
    print(sqnon_str)


if __name__ == "__main__":
    main()
