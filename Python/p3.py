class Solution(object):
    def commonChars(self, words):
        common=[]
        for char in words[0]:
            c=0
            for j in range(1,len(words)):
                if char in words[j]:
                    c+=1
            if c==len(words)-1:
                common.append(char)
                for k in range(1,len(words)):
                    words[k]=words[k].replace(char,'',1)
        return common

#since i didn't use hashmap it's a code with a time complexity of o(n^3) 
#but it's stil fast and beats 88% of users with python. 
