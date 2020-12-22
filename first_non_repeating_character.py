# find the first non-repeating character in a string. The second solution increases the space complexity while reducing
# time complexity


from collections import defaultdict
from time import time
from random import randrange


def measure_time(fn):                   # time measuring decorator
    def wrapper(*args, **kwargs):
        start = time()
        fn(*args, **kwargs)
        end = time()
        return end - start

    return wrapper


def random_string_generator():
    return "".join(chr(randrange(97, 123)) for _ in range(10000))


@measure_time
def brute_force(s):                     # O(n^2) time complexity
    for c in s:
        if s.count(c) == 1:
            return c
    return "_"


@measure_time
def space_complex_solution(s):          # O(n) time complexity
    d = defaultdict(int)
    for c in s:                         # O(n)
        d[c] += 1
    for c, occurrence in d.items():     # O(n)
        if occurrence == 1:
            return c
    return "_"


def main():
    brute_force_times = []
    space_complex_solution_times = []
    for run in range(1000):
        s = random_string_generator()
        brute_force_times.append(brute_force(s))
        space_complex_solution_times.append((space_complex_solution(s)))

    brute_force_times_average = sum(brute_force_times) / 1000
    space_complex_times_average = sum(space_complex_solution_times) / 1000
    ratio = brute_force_times_average / space_complex_times_average

    print(f"Time average of 1000 brute force runs with a random 10000 character string: {brute_force_times_average}")
    print(f"Time average of 1000 space complex runs with a random 10000 character string: {space_complex_times_average}")
    print(f"The space complex solution is {ratio:.2f} times faster than the brute force solution")



if __name__ == '__main__':
    main()
