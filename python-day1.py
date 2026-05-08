#type casting
'''a=int(input())
print(a)
print(type(a))
b=int(input())
print(b)
print(type(b))'''
#Arithmetic operator
a=int(input("enter the value"))
b=int(input("enter the value"))
print("addition",a+b)
print("its subtraction",a-b)
print("multiplication",a*b)
print("floor division",a/b)
print("integer division",a//b)
print("remainder",a%b)
print("exponentiation",a**b)

#Assignment operator
'''n=4
n1=n+2
print(n)
print(n1)'''

n=3
print(n)
n*=2 #n=n*2
print(n)

x=5
x+=5
print(x)

#comparison/relational  operator

age1=17
age2=13
print(age1==age2)
print(age1!=age2)
print(age1>age2)
print(age1<age2)
print(age1>=age2)
print(age1<=age2)

#logical operator

level=20
health=7
if(level>25) and (health>5):
    print("next level")
else:
    print("failed")

level=20
health=7
if(level>25) or (health>5):
    print("next level")
else:
    print("failed")
    
a=True
print(not(a))

a=10
if not(a>15):
    print("greater")
else:
    print("less")


#special operators
#identity operator

rithika=["chocolates","chips"]
nimalan=["chocolates","chips"]
print(rithika is not nimalan)


jayanth=nimalan
print(jayanth is nimalan)

#membership operator


s=["r","s","n","l","j"]
if "z" not in s:
    print("present")
else:
    print("not present")


x = ["apple", "banana"]
print("banana" in x)


#bitwise operators
a=9
b=12
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<3)    
print(a>>3)

























