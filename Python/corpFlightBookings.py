class Solution(object):
    def corpFlightBookings(self, bookings, n):
        ans=[0]*n
        for f,l,s in bookings:
            ans[f-1]+=s
            if l<n:
                ans[l]-=s
        for i in range(1,n):
            ans[i]+=ans[i-1]
        return ans




        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """
        
