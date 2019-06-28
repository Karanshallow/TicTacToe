class TicTacTree(object):
    def __init__(self):
        self.blank = None
        self.is9 = None
        self.is8 = None
        self.is7 = None
        self.is6 = None
        self.is5 = None
        self.is4 = None
        self.is3 = None
        self.is2 = None
        self.is1 = None
        self.data = 0
    def next(self,var):
        if var == 9:
            if self.is9 != None:
               return self.is9.data
        elif var == 8:
            if self.is8 != None:
                return self.is8.data
        elif var ==7:
            if self.is7 != None:
                return self.is7.data
        elif var ==6:
            if self.is6 != None:
                return self.is6.data
        elif var ==5:
            if self.is5 != None:
                return self.is5.data
        elif var == 4:
            if self.is4 != None:
                return self.is4.data
        elif var == 3:
            if self.is3 != None:
                return self.is3.data
        elif var == 2:
            if self.is2 != None:
                return self.is2.data
        elif var ==1:
            if self.is1 != None:
                return self.is1.data
        else:
            return None
                
        
        

        
