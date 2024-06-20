class Solution(object):
    def sortPeople(self, names, heights):
        zipped=list(zip(names,heights)) 
        zipped.sort(key=lambda item:item[1])
        zipped.reverse()
        print(zipped)
        ans=[]
        for name in zipped:
            ans.append(name[0])    
        return ans

