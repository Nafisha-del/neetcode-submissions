# 128. Longest Consecutive Sequence https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # numSet = set(nums)
        # longest = 0
        # for n in nums:
        #     # Check if it is a start of a sequence
        #     if (n-1) not in numSet:
        #         length = 0
        #         while (n+length) in numSet:
        #             length += 1
        #         longest = max(length, longest)
        # return longest

        # Initial Solution
        if not nums:
            return 0
        sorted_nums = sorted(set(nums))
        longest = 1
        seq = 1
        i = 1
        while i < len(sorted_nums):
            if sorted_nums[i] == sorted_nums[i - 1] + 1:
                seq += 1
            else:
                seq = 1
            longest = max(longest, seq)
            i += 1
        return longest
