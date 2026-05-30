"""Given an array of integers temperatures represents the daily temperatures, 
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0 instead."""


def dailyTemperatures(self, temp: List[int]) -> List[int]:
    stack = []
    answers = [0]*len(temp)
    for i in range(len(temp)):
        while stack and temp[i] > temp[stack[-1]]:
            idx = stack.pop()
            answers[idx] = i-idx
        stack.append(i)
    return answers
