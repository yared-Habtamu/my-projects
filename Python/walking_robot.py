class Robot:

    def __init__(self, w: int, h: int):

        self.build = {0:[[0, 0], 'e']}
        self.moves = 0
        self.isMoved = False
        
        x, y = 1, 0
        d = 'e'
        count = 1
        while x or y:
            
            self.build[count] = [[x, y], d]
            
            
            if x == w - 1 and d == 'e':
                d = 'n'
            if y == h - 1 and d == 'n':
                d = 'w'
            if x == 0 and d == 'w':
                d = 's'
  
            
            
            if d == 'e':
                x += 1
                
            if d == 'n':
                y += 1
            if d == 'w':
                x -= 1
            if d == 's':
                y -= 1
            
            count += 1
        
        # print(self.build)
    

    def step(self, num: int) -> None:
        self.isMoved = True
        self.moves += num
        self.moves %= len(self.build)
 
    def getPos(self) -> List[int]:
        
        pos, d = self.build[self.moves]
        
        return pos
        

    def getDir(self) -> str:
        
        pos, d = self.build[self.moves]
        
        dirMap = {'e':'East', 'n': 'North', 's':"South", 'w': 'West'}
        
        
        if self.isMoved and self.moves == 0:
            return 'South'
        
        return dirMap[d]
        """
        :rtype: List[int]
        """
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
