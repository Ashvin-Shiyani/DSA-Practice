def rainwater(height):
    if not height:
        return 0

    l, r = 0, len(height)-1
    maxleft, maxright = height[l], height[r]
    cap = 0
    while l < r:
        if maxleft < maxright:
            l += 1
            maxleft = max(maxleft, height[l])
            cap += maxleft-height[l]
        else:
            r -= 1
            maxright = max(maxright, height[r])
            cap += maxright-height[r]
    return cap


print(rainwater([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
