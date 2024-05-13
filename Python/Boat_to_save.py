class Solution(object):
    def numRescueBoats(self, people, limit):
        c=0
        l,r=0,len(people)-1
        people.sort()
        while l<=r:
            if people[l]+people[r]<=limit:
                l+=1
                r-=1
            else:
                r-=1

            c+=1
        return c
