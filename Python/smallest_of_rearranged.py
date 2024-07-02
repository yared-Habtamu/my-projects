class Solution(object):
    def smallestNumber(self, num):
        if num == 0:
            return 0    
        isNegative, nums, countZero, s = False, [], 0, str(num)       
        if  num < 0:
            isNegative = True
            s = s[1:]
        for i in range(len(s)):
            if s[i] != '0':
                nums.append(s[i])
            else:
                countZero += 1

        nums.sort(reverse=isNegative)
        newN = ''.join(nums)

        if isNegative:
            return int('-' + newN + '0' * countZero)

        return int(newN[0] + '0' * countZero + newN[1:])
    
            






        """
        :type num: int
        :rtype: int
        """
        
