class Solution(object):
    def isValid(self, s):
        list2=[]
        for i in range(0,len(s)-1):
            if s[i]=='(':
                for j in range(i+1,len(s)):
                    if s[j]==')':
                        list2.append(s[i])
                        list2.append(s[j])
                    elif j==len(s):
                        list2.append(s[i])
            elif s[i]=='[':
                for j in range(i+1,len(s)):
                    if s[j]==']':
                        list2.append(s[i])
                        list2.append(s[j])
                    elif j==len(s):
                        list2.append(s[i])          
            elif s[i]=='{':
                for j in range(i+1,len(s)):
                    if s[j]=='}':
                        list2.append(s[i])
                        list2.append(s[j])
                    elif j==len(s):
                        list2.append(s[i])
        if (len(list2)%2)!=0:
            return False
        return True

 
