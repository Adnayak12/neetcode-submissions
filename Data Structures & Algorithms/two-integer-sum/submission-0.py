class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    sum_total = nums[i] + nums[j]
                    if sum_total == target:
                        return [min(i, j), max(i, j)]