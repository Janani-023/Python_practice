'''class Dog:
    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name
        print(name)

    def add_trick(self, trick):
        self.tricks.append(trick)
        print(self.tricks)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')




class Student:

    def __init__(self,n,c):
        self.name=n
        self.course=c

    def f(self):
        print("hello")
o=Student("dharani","ai")
print(o.name)
o.f()



#inhertiance


#types-single inheritance
class Hero:
    def attack(self):
        print("power")
class Ironman(Hero):
    def laser(self):
        print("laser activated..")

i=Ironman()
i.laser()

#multilevel inheritance

class Hero:
    def attack(self):
        print("power")
class Ironman(Hero):
    def laser(self):
        print("laser activated..")
class UltiIronman(Ironman):
    def healing():
        print("healing activated..")
i=UltiIronman()
i.attack()
'''
#hierari=chical
class Hero:
    def attack(self):
        print("power")
class Ironman(Hero):
    def laser(self):
        print("laser activated..")
class Spiderman(Hero):
    def web(self):
        print("web power..")
i=Ironman()
s=Spiderman()



#mutiple
class scientist:
    def study(self):
        print("researcher")
class spiderpower:
    def spider(self):
        print("power..")
class spiderman(scientist,spiderpower):
    def spiderman(self):
        print("spiderman created....")
c=spiderman()
c.spider()
c.study()
c.spiderman()











