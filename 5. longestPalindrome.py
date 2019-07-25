class Solution:
    # def get_l(self, t: str, i: int) -> int:
    #     lf, rt = i - 1, i + 1
    #     c = 0
    #     while lf >= 0 and rt < len(t) and t[lf] == t[rt]:
    #         c += 1
    #         lf -= 1
    #         rt += 1
    #     return c

    def longestPalindrome(self, s: str) -> str:
        # length = len(s)
        # if length == 0:
        #     return ''
        # if length == 1:
        #     return s
        # t = ''
        # index = 0
        # while index < 2 * length + 1:
        #     if index % 2 == 0:
        #         t += '#'
        #     else:
        #         t += s[(index - 1) // 2]
        #     index += 1
        # start, max_len = 0, 1
        # for i in range(2, len(t)):
        #     s_len = self.get_l(t, i)
        #     if s_len > max_len:
        #         max_len = s_len
        #         start = i // 2 - s_len // 2
        # return s[start:start + max_len]
        if (len(s) <= 1) or s == s[::-1]:
            return s
        start = 0
        maxlen = 0
        for i in range(len(s)):
            str1 = s[i - maxlen: i + 1]
            str2 = s[i - maxlen - 1: i + 1]
            
            if (i - maxlen) >= 0 and (str1 == str1[::-1]):
                start, maxlen = i - maxlen, len(str1)
            if (i - maxlen - 1) >= 0 and (str2 == str2[::-1]):
                start, maxlen = i - maxlen - 1, len(str2)
        return s[start: start + maxlen]
        
