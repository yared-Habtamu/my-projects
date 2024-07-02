class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        right=len(numbers)-1
        left=0
        ans=[]
        while right>left:
            if (numbers[right]+numbers[left])>target:
                right-=1
            elif(numbers[right]+numbers[left])<target:
                left+=1
            else:
                ans.append(left+1)
                ans.append(right+1)
                break
        return ans
