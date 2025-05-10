# https://leetcode.com/problems/group-anagrams/
# wrong solution but the idea is good if there is an assumption that count of each letter doesn't have to be the same
# need to get back

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            fs = frozenset(s)
            a = d.get(fs, [])
            a.append(s)
            a.sort()
            d[fs] = a
        
        return list(d.values())