class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return len(nums) != len(set(nums))
            seen.add(n)
        return len(nums) != len(set(nums))
