class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            neededNum = target - num
            if neededNum in hashmap:
                return [i, hashmap[neededNum]]
            hashmap[num] = i
        
            