class sample:
    def __init__(self,name):
        print("hi im constructor")
        self.name=name
        print(self.name)
    def __del__(self):
        print("object is deleted")
s=sample("janani")
del s #this will call the __del__() fun


#polymorphism
#runtime polymorphism/method overriding
class Alien:
    def power(self):
        pass
class Fourarms(Alien):
    def power(self):
        print(" super strength")
class Heatblast(Alien):
    def power(self):
        print("fire blast ")
class XLR8(Alien):
    def power(self):
        print("super speed")
aliens=[XLR8(),Fourarms(),Heatblast()]
for alien in aliens:
    alien.power()

#compile time /method overloading
class Calculator:
    def add(self,a,b=0,c=0):
        print(a+b+c)

c=Calculator()
c.add(10,50,90)
c.add(7,9)
c.add(8)

#use type checks
class DataProcessor:
    def process(self, data):
        if isinstance(data, list):
            return [x * 2 for x in data]
        elif isinstance(data, str):
            return data.upper()
        return data

processor = DataProcessor()
print(processor.process([1, 2])) # Output: [2, 4]
print(processor.process("hi"))   # Output: "HI"






