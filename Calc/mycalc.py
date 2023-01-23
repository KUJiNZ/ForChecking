class Calculator:
    def __init__(self,x,y):
        """
        Like a constructor.
        When creating instance of some class this function is first to calling.
        """
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x - self.y

    def mult(self):
        return self.x * self.y

    def div(self):
        if not self.y == 0:
            return self.x / self.y
        else:
            return 0
