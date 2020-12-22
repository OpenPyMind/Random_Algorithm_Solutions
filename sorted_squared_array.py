# solution to "sorted squared integer array" algorithm problem. The input array is sorted, and values can be both
# positive and negative, and the output has to be sorted as well.
# Solution:
#   - create an empty array with the same length as the input array
#   - by use of pointer variables, start left at 0 and right at the last valid index
#   - iterate backwards through the output array
#   - if the value at the right pointer is larger than or equal to the value at the left pointer, replace the value
#   at the given index in the output array with the "right number", increment right pointer by 1
#   - in the other scenario, replace value at given index in output array by "left number", and decrement left pointer
#   by 1


def sorted_squared_fn(ar):
    sorted_squared = [0 for _ in range(len(ar))]        # "empty" output array
    pointer_left = 0
    pointer_right = len(ar) - 1
    for idx in range(len(ar) - 1, -1, -1):
        number_left = abs(ar[pointer_left])
        number_right = abs(ar[pointer_right])

        take_left = number_left >= number_right
        if take_left:
            sorted_squared[idx] = number_left ** 2
            pointer_left += 1
        else:
            sorted_squared[idx] = number_right ** 2
            pointer_right -= 1

    return sorted_squared


def main():
    array = [-4, -2, -1, 0, 1, 3, 4, 5]
    print(sorted_squared_fn(array))


if __name__ == '__main__':
    main()