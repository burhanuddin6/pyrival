# https://leetcode.com/problems/group-anagrams/
# Beats 50% (not much difference from the best)
# look at the lines of code, that's why i love python.

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        # isAnagram is intelligent. not me.
        def isAnagram(a, b):
            return sorted(a) == sorted(b)

        strs_dict = {}
        for string in strs:
            s_string = str(sorted(string))
            if s_string in strs_dict:
                strs_dict[s_string].append(string)
            else:
                strs_dict[s_string] = [string]
        
        return list(strs_dict.values())
