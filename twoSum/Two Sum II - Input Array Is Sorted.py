class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                return [l + 1, r + 1]
            elif s < target:
                l += 1
            else:
                r -= 1


def test_twoSum():
    solution = Solution()

    # Test case 1
    numbers = [2, 7, 11, 15]
    target = 9
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected

    # Test case 2
    numbers = [2, 3, 4]
    target = 6
    expected = [1, 3]
    assert solution.twoSum(numbers, target) == expected

    # Test case 3
    numbers = [-1, 0]
    target = -1
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected

    # Test case 4
    numbers = [3, 3]
    target = 6
    expected = [1, 2]
    assert solution.twoSum(numbers, target) == expected

    print("All test cases pass")


test_twoSum()
