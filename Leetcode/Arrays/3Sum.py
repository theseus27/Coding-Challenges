#Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. Notice that the solution set must not contain duplicate triplets.

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    assert(i != j and i != k and j != k)
                    inOrder = sorted([nums[i], nums[j], nums[k]])
                    if (sum(inOrder) == 0 and inOrder not in results):
                        results.append(inOrder)
        return results
                    