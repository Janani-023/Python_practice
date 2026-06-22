'''from abc import ABC,abstractmethod#abtract module/library
import Abss
class Animal(ABC):#inherited the abc class
    @abstractmethod#decorator
    def sound(self):#abstract method
        pass

class Dog(Animal):
     def sound(self):
        print("barking")

class Cat(Animal):
     def sound(self):
         print("meowing")
d=Dog()
d.sound()
c=Cat()
c.sound()
  
#d=Animal()
#d.sound()'''


from abc import ABC,abstractmethod

class FoodDeliveryApp(ABC):
    @abstractmethod
    def deliver(self):
        pass
class Zomato(FoodDeliveryApp):
    def deliver(self):
        print("food delivery by zomato")
class Swiggy(FoodDeliveryApp):
    def deliver(self):
        print("food delivery by swiggy")
z=Zomato()
z.deliver()

