#!/usr/bin/env python3

class Shoe:
    
    def __init__(self, brand, size, condition="used"):
        self.brand = brand
        self.size = size
        self.condition = condition
        

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
            self._size = None
        else:
            self._size = value

    

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"
        return True


    @property
    def condition(self):
        return self._condition
    
    @condition.setter
    def condition(self, value):
        self._condition = value
        

    
        
        
    

 
    


