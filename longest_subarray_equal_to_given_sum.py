# solution to finding the maximum length contiguous subarray in a positive integer array with a given sum
#   - set left and right pointers to the beginning of the array
#   - while the right pointer is equal or greater than the left pointer and less than the size of the array:
#       - increment right pointer by 1 as long as the current sum of the subarray is less than the given sum
#       - increment left pointer by 1 as long as current sum of the subarray is larger than the given sum
#       - upon finding the given sum equals the sum of a subarray, save the subaray index boundaries,
#       increment right pointer by 1. Will overwrite subarray boundaries if the current subarray is longer than
#       already found one
#       - this will overshoot the given sum (unless next element is 0), and we will move the pointers until all
#       subarray sums and the lenght of the corresponding subarrays have been assayed.


ar_1 = [15, 1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
s_1 = 15
ar_2 = [1, 2, 3, 7, 5]
s_2 = 12


def find_longest_subarray(array, s):  # O(n) time complexity
    left_pointer = 0
    right_pointer = 0
    max_subarray = [-1, 0]      # idx 1: length, idx 0: indices in original array

    while left_pointer <= right_pointer < len(array):
        current_subarray_sum = sum(array[left_pointer:right_pointer + 1])
        if current_subarray_sum < s:
            right_pointer += 1
        elif current_subarray_sum > s:
            left_pointer += 1
        else:
            subarray_length = len(array[left_pointer:right_pointer + 1])
            if subarray_length > max_subarray[1]:
                max_subarray[1] = subarray_length
                max_subarray[0] = [left_pointer, right_pointer]
            right_pointer += 1

    return max_subarray[0]


def main():
    print(find_longest_subarray(ar_1, s_1))
    print(find_longest_subarray(ar_2, s_2))


if __name__ == '__main__':
    main()






