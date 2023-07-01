def three_sum_closest(nums, target):
    """
    Finds three integers in nums such that the sum is closest to target.

    Args:
      nums: An integer array of length n.
      target: An integer.

    Returns:
      The sum of the three integers.
    """

    nums.sort()
    closest_sum = float("inf")
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum
            if current_sum < target:
                left += 1
            else:
                right -= 1
    return closest_sum


def test_three_sum_closest():
    assert three_sum_closest([1, 2, 3, 4, 5], 10) == 10
    assert three_sum_closest([1, 2, 3, 4, 5], 7) == 7
    assert three_sum_closest([-1, 2, 1, -4], 1) == 2
    assert three_sum_closest([0, 0, 0], 1) == 0


if __name__ == "__main__":
    test_three_sum_closest()
