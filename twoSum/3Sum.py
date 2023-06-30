from typing import List


def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    l = []
    for i in range(len(nums)):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s > 0:
                k -= 1
            elif s < 0:
                j += 1
            else:
                l.append([nums[i], nums[j], nums[k]])
                j += 1
                while nums[j - 1] == nums[j] and j < k:
                    j += 1
    return l


# def threeSum(self, nums: List[int]) -> List[List[int]]:
#     nums.sort()
#     result = []
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             for k in range(j + 1, len(nums)):
#                 if nums[i] + nums[j] + nums[k] == 0:
#                     result.append([nums[i], nums[j], nums[k]])
#     return result


nums = [-1, 0, 1, 2, -1, -4]

result = threeSum(nums)
print(result)
