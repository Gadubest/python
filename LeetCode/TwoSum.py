class Solution:
    def twoSum(self, nums, target):
        for i in range(0,nums.__len__()):
            heuristic = target-nums[i]
            if(nums.__contains__(heuristic)):
                if(nums.index(heuristic)!=i):
                    return [i,nums.index(heuristic)]


#https://leetcode.com/problems/two-sum/