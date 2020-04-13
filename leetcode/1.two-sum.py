#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict(zip(nums, range(len(nums))))
        for i, n in enumerate(nums):
            y = target - n
            try:
                index2 = hm[y]
                index1 = i
                if index1 == index2:
                    continue
                else:
                    return [index1, index2]
            except KeyError:
                pass

# @lc code=end
