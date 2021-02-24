class my_class():
    def __init__(self,input1=0,input2=0):
        self.input1=input1
        self.input2=input2

    def first_fun(self):
        self.add=self.input1+self.input2
        self.mult=self.input1 * self.input2
        print(type(self))
        print(self.add)
        print(self.mult)

my_obj1=my_class(12,12)
my_obj1.first_fun()

