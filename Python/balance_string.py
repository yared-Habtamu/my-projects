class Solution:
    def balancedString(self, s):
        count = collections.Counter(s)
        print(count)
        res = n = len(s)
        if all(n/4==count[char] for char in 'QWER'):
            return 0
        left = 0
        for right, char in enumerate(s):
            count[char] -= 1
            while left <= right and all(n / 4 >= count[char] for char in 'QWER'):
                res = min(res, right - left + 1)
                count[s[left]] =count[s[left]]+ 1
                left += 1
        return res
    

        return 2
        """
        :type s: str
        :rtype: int
        """
        
