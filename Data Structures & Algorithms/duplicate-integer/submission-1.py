class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        for n in nums:
            if n not in nums_dict:
                nums_dict[n] = 0
            if n in nums_dict:
                nums_dict[n] += 1

        for val in nums_dict.values():
            if val > 1:
                return True
        return False