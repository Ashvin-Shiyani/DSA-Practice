"""Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order."""


def topKFrequent(nums, k: int):
    freq = {}
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]
