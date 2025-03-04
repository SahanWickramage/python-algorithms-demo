def main():
    nums = [2, 3, 1, 2, 4, 3]
    S = 7
    print(min_subarray_len(S, nums))


def min_subarray_len(S, nums):
    min_length = float('inf')
    window_sum = 0
    start = 0

    for end in range(len(nums)):
        window_sum += nums[end]  # Expand window

        while window_sum >= S:  # Shrink when condition met
            min_length = min(min_length, end - start + 1)
            window_sum -= nums[start]
            start += 1

    return min_length if min_length != float('inf') else 0


if __name__ == "__main__":
    main()
