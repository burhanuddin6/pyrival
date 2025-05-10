# https://leetcode.com/problems/top-k-frequent-elements/

# beats 50%
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counts = Counter(nums)
        c = counts.most_common(k)
        return [k[0] for k in c]

