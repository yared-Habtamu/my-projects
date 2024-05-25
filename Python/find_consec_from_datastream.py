class DataStream:

    def __init__(self, value: int, k: int):
        self.k = k
        self.val = value
        self.t = k
        

    def consec(self, num: int) -> bool:
        if self.t > 0:
            self.t -= 1
            
        if num != self.val:
            self.t = self.k
        
        if self.t:
            return False
        return True


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
