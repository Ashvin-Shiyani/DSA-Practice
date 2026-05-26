'''Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.'''


def threeSum(self, nums: list[int]) -> list[list[int]]:
    nums.sort()
    result = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        start = i+1
        end = len(nums)-1
        while start < end:
            sum = nums[i]+nums[start]+nums[end]
            if sum == 0:
                num = [nums[i], nums[start], nums[end]]
                result.append(num)
                start += 1
                end -= 1
                while start < end and nums[start] == nums[start-1]:
                    start += 1

            if sum < 0:
                start += 1
            if sum > 0:
                end -= 1
    return result
