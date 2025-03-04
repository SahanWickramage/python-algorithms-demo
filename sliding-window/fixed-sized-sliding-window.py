def main():
    nums = [2, 1, 5, 1, 3, 2]
    k = 3
    print(max_sum_subarray(nums, k))


def max_sum_subarray(nums, k):
    max_sum, window_sum, start = 0, 0, 0
    for end in range(len(nums)):
        window_sum += nums[end]
        if end >= k - 1:
            max_sum = max(max_sum, window_sum)
            window_sum -= nums[start]
            start += 1
    return max_sum


if __name__ == "__main__":
    main()
