class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxlength = 0

        for i in nums:
            if (i-1) not in numSet:
                length = 1
                while (i+length) in numSet: # + length because thats how you increment by 1, i is not getting adjusted in this loop
                    length += 1
                maxlength = max(length, maxlength)
        return maxlength