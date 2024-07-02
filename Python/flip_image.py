class Solution(object):
    def flipAndInvertImage(self, image):
        for arr in image:
            arr.reverse()
            for i in range(len(arr)):
                if arr[i]==0:
                    arr[i]=1
                else:
                    arr[i]=0
        return image
