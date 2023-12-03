"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""




class Solution(object):
    def is_present(self, strs, smallest_word):
        for word in strs:
            if not word.startswith(smallest_word):
                return False
        return True
                   
    
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        str_len = []
        str_dict = {}
        strs = set(strs)
        for item in set(strs):
            str_len.append(len(item))
            str_dict[len(item)] = item

        strs = sorted(strs, key=len)
        smallest_word = strs[0]
        
        for i in range(0, len(smallest_word)):
            present = self.is_present(strs, smallest_word)
            if present:
                break
            else:
                smallest_word = smallest_word[:(len(smallest_word)-1)]
                
        return smallest_word

strs = ["flower", "ffaa", "flow","flight"]
obj = Solution()
ret = obj.longestCommonPrefix(strs)
print(ret, type(ret))