
def productExceptSelf(nums):
    left = [1]
    for i in range(1, len(nums)):
        value = left[i-1]*nums[i-1]
        left.append(value)
    temp_nums = nums[::-1]
    right = [1]
    for i in range(1, len(temp_nums)):
        value = right[i-1]*temp_nums[i-1]
        right.append(value)

    right = right[::-1]
    result = []
    for i in range(0, len(nums)):
        result.append(left[i]*right[i])
    return result


ashu = [1, 2, 3, 4]
print(productExceptSelf(ashu))
