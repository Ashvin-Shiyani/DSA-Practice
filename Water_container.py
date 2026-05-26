
def maxArea(height):
    start = 0
    end = len(height)-1
    maxWater = 0
    while start < end:
        water = min(height[start], height[end])*(end-start)
        maxWater = max(maxWater, water)

        if height[start] < height[end]:
            start += 1
        else:
            end -= 1

    return maxWater


print(maxArea([1, 8, 6, 2, 5, 4, 7, 3, 8]))
