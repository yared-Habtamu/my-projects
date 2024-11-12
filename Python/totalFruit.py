class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        fruit1,fruit1_idx,fruit2,fruit2_idx = None,None,None,None
        ans=0
        left=-1

        for idx, fruit in enumerate(fruits):
            if fruit1==None:
                fruit1=fruit
                fruit1_idx=idx
            elif fruit==fruit1:
                fruit1_idx=idx
            elif fruit2==None:
                fruit2=fruit
                fruit2_idx=idx
            elif fruit==fruit2:
                fruit2_idx=idx
            else:
                if fruit1_idx<fruit2_idx:
                    left=fruit1_idx
                    fruit1=fruit
                    fruit1_idx=idx
                else:
                    left=fruit2_idx
                    fruit2=fruit
                    fruit2_idx=idx
            
            ans=max(ans,idx-left)
        
        return ans
