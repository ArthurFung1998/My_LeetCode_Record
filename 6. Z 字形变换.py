class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        ans = [''] * numRows
        dr = True
        row = 0
        for c in s:
            ans[row] += c
            if dr:
                if row == numRows - 1:
                    dr = False
                    row -= 1
                else:
                    row += 1
            else:
                if row == 0:
                    dr = True
                    row += 1
                else:
                    row -= 1
                    
        return ''.join(ans) 
