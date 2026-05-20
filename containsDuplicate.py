"""Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct."""


def containsDuplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        else:
            seen.add(n)
    return False
