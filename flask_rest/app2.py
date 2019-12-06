class Calc:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def add(self):
       return self.a+self.b


if __name__ == '__main__':
    calc=Calc(1,2)
    print(calc.add())

