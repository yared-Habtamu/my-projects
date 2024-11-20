class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):
        start=0
        end=0
        length=0
        count_of_true=0
        count_of_false=0

        while end<len(answerKey):
            if answerKey[end]=='T':
                count_of_true+=1 
            else:
                count_of_false+=1 
            
            
            while(min(count_of_false,count_of_true)>k):
                if answerKey[start]=='T':
                    count_of_true-=1 
                else:
                    count_of_false-=1 
                start+=1 
            
            end+=1 
            length =max(length,count_of_true+count_of_false)

        return(length) 
