class Solution:
    def findMaximumScore(self, nums: List[int]) -> int:
        arr = nums
        nextGreaterEqual = [len(arr) - 1] * len(arr)
        stack = []
        for i in range(len(arr)):
            while stack and arr[stack[-1]] < arr[i]:
                nextGreaterEqual[stack.pop()] = i
            stack.append(i)

        curr_index = 0
        res = 0
        while True:
            if curr_index == len(arr) - 1:
                return res
            ngi = nextGreaterEqual[curr_index]
            curr_val = arr[curr_index]
            res += (ngi - curr_index) * curr_val
            curr_index = ngi
