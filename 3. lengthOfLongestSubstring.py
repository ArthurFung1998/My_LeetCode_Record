class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = ''
        maxLength = 0
        for i in s:
            if i not in subs:
                subs += i
            else:
                index = subs.index(i)
                subs = subs[index+1:]
                subs += i
            if len(subs) > maxLength:
                maxLength = len(subs)
        return maxLength
