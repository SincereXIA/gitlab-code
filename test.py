from typing import *

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j]
                    nums[j] = nums[j+1]
                    nums[j+1] = tmp
        return nums

if __name__ == "__main__":
    s = Solution()
    rs = s.sortArray([5, 4, 2, 1])
    print(rs)