class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        n = len(nums)
        result = 0

        for i in range(n):
            cnt = 0
            for j in range(i, n):
                if nums[j] == 0: break
                cnt += 1
            result = max(result, cnt)

        return result
        
        