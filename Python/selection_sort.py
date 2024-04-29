class Solution: 
    def select(self, arr, i):
        pass
         # code here 
    
    def selectionSort(self, arr, n):
        for i in range(n):
            for j in range(i + 1, n): 
                if arr[j] < arr[i]: 
                    temp=arr[j]
                    arr[j]=arr[i]
                    arr[i]=temp
        return arr
  #geeks 4 geeks
