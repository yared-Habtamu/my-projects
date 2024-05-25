class Solution(object):
    def removeDuplicateLetters(self, s):
        used = set()
        c = [0] * 26
        a = ord('a')
        for char in s:
            c[ord(char) - a] += 1
        ans = []
        for char in s:
            if len(ans) == 0:
                used.add(char)
                ans.append(char)
            elif char not in used and char > ans[-1]:
                used.add(char)
                ans.append(char)
            elif char not in used:
                while ans and ans[-1] >= char and c[ord(ans[-1]) - a] > 0:
                    delete_char = ans.pop()
                    used.discard(delete_char)
                used.add(char)
                ans.append(char)
            c[ord(char) - a] -= 1
        return ''.join(ans)
        """
        :type s: str
        :rtype: str
        """
        
