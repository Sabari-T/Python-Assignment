class Calc():
    def __init__(self,x,y):
        self.one=x
        self.two=y
    def add(self):
        return self.one+self.two
    def sub(self):
        return self.one-self.two
    def mul(self):
        return self.one*self.two
    def div(self):
        return self.one//self.two
result=Calc(7,5)
print(result.add())
print(result.sub())
print(result.mul())
print(result.div())